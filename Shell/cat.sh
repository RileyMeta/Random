#!/bin/bash

# This is essentially a clone of the `cat` Core Util written in bash
packages=$1

while IFS= read -r package; do
    echo "$package"
done < "$packages"

# Yeah, this is about it
