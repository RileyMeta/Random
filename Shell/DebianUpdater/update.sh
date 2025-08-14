#!/usr/bin/env bash

set -euo pipefail

# Default flags
VERBOSE=false
SIMULATE=false
FORCE=false

# Functions
usage() {
    cat <<EOF
Usage: $0 [options]

Options:
  -v    Verbose mode (show full apt output)
  -s    Simulation mode (dry-run before upgrade)
  -i    Show current and next Debian codename
  -f    Force mode (skip confirmation prompts)
  -h    Show this help message

Examples:
  $0 -s       Simulate upgrade only
  $0 -v       Upgrade with verbose apt output
  $0 -v -s    Simulate first, then verbose upgrade
  $0 -f       Upgrade without confirmation prompts
EOF
}

info() {
    echo "Current release: $current_codename"
    echo "Next release:    $next_codename"
}

simulate_upgrade() {
    echo "Simulating upgrade..."
    local output
    output=$(apt -s full-upgrade 2>/dev/null)

    local upgrades installs removals
    upgrades=$(grep -E "upgraded," <<< "$output" | awk '{print $1}')
    installs=$(grep -E "upgraded," <<< "$output" | awk '{print $4}')
    removals=$(grep -E "upgraded," <<< "$output" | awk '{print $6}')

    echo
    echo "Summary of simulated upgrade:"
    echo "  Packages to be upgraded: $upgrades"
    echo "  Packages to be installed: $installs"
    echo "  Packages to be removed:   $removals"
    echo
    echo "Full package list:"
    apt -s full-upgrade | grep -E "Inst|Remv" || true
    echo
}

# Root check
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root."
    exit 1
fi

# Ensure required package
if ! command -v lsb_release &>/dev/null || [ ! -f /usr/share/distro-info/debian.csv ]; then
    echo "Installing required package: distro-info-data"
    apt update && apt install -y distro-info-data lsb-release
fi

# Detect releases
current_codename=$(lsb_release -cs)
next_codename=$(awk -F',' -v cur="$current_codename" '
    $2 == cur {getline; print $2}
' /usr/share/distro-info/debian.csv)

if [[ -z "$next_codename" ]]; then
    echo "Error: Could not find a newer Debian release after $current_codename."
    exit 1
fi

# Parse options
while getopts "vsifh" opt; do
    case "$opt" in
        v) VERBOSE=true ;;
        s) SIMULATE=true ;;
        i) info; exit 0 ;;
        f) FORCE=true ;;
        h) usage; exit 0 ;;
        *) usage; exit 1 ;;
    esac
done

# Optional simulation
if $SIMULATE; then
    simulate_upgrade
    if ! $FORCE; then
        read -rp "Proceed with actual upgrade from $current_codename to $next_codename? (y/N) " confirm
        if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
            echo "Upgrade cancelled."
            exit 0
        fi
    fi
fi

# Final confirmation
if ! $FORCE; then
    echo "This will upgrade your system from $current_codename → $next_codename."
    read -rp "Continue? (y/N) " confirm
    if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
        echo "Upgrade cancelled."
        exit 0
    fi
fi

# Pre-upgrade
apt update
apt full-upgrade -y ${VERBOSE:+-o Debug::pkgProblemResolver=true}

# Backup sources
cp /etc/apt/sources.list /etc/apt/sources.list.bak.$(date +%F)
if [ -f "/etc/apt/sources.list.d/debian.sources" ]; then
    cp /etc/apt/sources.list.d/debian.sources /etc/apt/sources.list.d/debian.sources.bak.$(date +%F)
fi

# Modify sources.list
if grep -q "$current_codename" /etc/apt/sources.list; then
    sed -i "s/$current_codename/$next_codename/g" /etc/apt/sources.list
else
    echo "No '$current_codename' entries in sources.list, skipping."
fi

# Modify deb822 format if present
if [ -f "/etc/apt/sources.list.d/debian.sources" ] && grep -qi "$current_codename" /etc/apt/sources.list.d/debian.sources; then
    sed -i "s/${current_codename^}/${next_codename^}/g" /etc/apt/sources.list.d/debian.sources
fi

# Perform upgrade
apt update
apt upgrade --without-new-pkgs -y ${VERBOSE:+-o Debug::pkgProblemResolver=true}
apt full-upgrade -y ${VERBOSE:+-o Debug::pkgProblemResolver=true}

# Clean up
apt autoremove --purge -y
apt clean

echo "Upgrade process complete. Please reboot your system."
