import subprocess
import requests

def get_installed_version():
    """Gets the installed NVIDIA driver version using pacman."""
    try:
        result = subprocess.run(["pacman", "-Q", "nvidia-open-dkms"], capture_output=True, text=True, check=True)
        version = result.stdout.split()[1]
        return version.split("-")[0]  # Extract version number (ignoring sub versions: -2, -3, etc)
    except subprocess.CalledProcessError:
        return None

def get_latest_version():
    """Fetches the latest NVIDIA driver version from the Arch Linux repository API."""
    url = "https://archlinux.org/packages/extra/x86_64/nvidia-open-dkms/json/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["pkgver"]  # Extract version number
    except requests.RequestException:
        return None

def check_for_update():
    installed = get_installed_version()
    latest = get_latest_version()

    if installed is None:
        print("NVIDIA driver is not installed.")
    elif latest is None:
        print("Could not fetch the latest driver version.")
    elif installed == latest:
        print(f"NVIDIA driver is up to date (Version: {installed}).")
    else:
        send_notification(latest)

def send_notification(version):
    subprocess.run(["notify-send", "Nvidia Driver Update Available", f"Version: {version}"])

if __name__ == "__main__":
    check_for_update()
