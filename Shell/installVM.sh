#!/bin/bash
# Guide Used to build this script
# https://gist.github.com/tatumroaquin/c6464e1ccaef40fd098a4f31db61ab22

main() {
        prompt="What would you like to do?"
        prompt+="\n1) Check System for VM Capabilities"
        prompt+="\n2) Would you like to use the Monolithic or the Modular Daemon?"
        echo -e $prompt
        read -p "> "
        case $REPLY in
                1) echo "Hello World" ;;
                2) echo "Goodbye World" ;;
        esac
}

main
