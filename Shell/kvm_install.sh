#!/bin/bash

_install_dependencies() {
    packages="qemu-full qemu-img libvirt virt-install virt-manager "
    packages+="virt-viewer edk2-ovmf swtpm guestfs-tools libosinfo tuned"
    sudo pacman -Sy $packages
    echo "Dependencies Installed"
}

_download_virtio() {
        local virtio_base_url="https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/archive-virtio/virtio-win-"
        local directory_url="https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/archive-virtio/"

        # Get the directory contents and extract the latest version from the file list
        local virtio_version=$(curl -s "$directory_url" | grep -oP 'virtio-win-\K[0-9]+\.[0-9]+\.[0-9]+-[0-9]+' | sort -V | tail -n 1)

        if [ -z "$virtio_version" ]; then
                echo "Error: Could not find the latest version."
                exit 1
        fi

        local virtio_link="${virtio_base_url}${virtio_version}/virtio-win.iso"

        wget -O ~/Downloads/virtio-win.iso $virtio_link
        echo "Virtio-win.iso | Download Complete!"
}

_enable_libvirt() {
    sudo systemctl enable libvirtd.service
    echo "Libvirt SystemD Service Started"
}

_create_network() {
    sudo virsh net-start default
    sudo virsh net-autostart default
    echo "Default Network Started"
}

_usermod_libvirt() {
    sudo usermod -aG libvirt $(whoami)
    echo "User added to the Libvirt Group"
}

main() {
    clear
    _install_dependencies
    _download_virtio
    _enable_libvirt
    _create_network
    _usermod_libvirt
    echo "Setup Complete"
}

main
