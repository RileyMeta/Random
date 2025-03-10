### A simple program tuned to look for common escape characters used in ASCII art and pad them for use in the shell.

ascii_art = ["You can t\est",
             "u$ing",
             "`these"]
# Ascii should be formatted this way, if using an ascii art generator it should print out strings with spaces.


def get_filename():
    print("Please input the name of the file:")
    while True:
        file_name = input().strip()
        if file_name:
            return f"{file_name}.sh"

def blank_slate(file_name):
    try:
        with open(file_name, "w") as f:
            f.write("#!/bin/bash\n")
    except Exception as e:
        print(f"Error: {e}")

def write_to_file(file_name, output):
    try:
        with open(file_name, "a") as f:
            f.write(f"echo \"{output}\"\n")
    except Exception as e:
        print(f"Error: {e}")

def proofer(file_name, _ascii):
    for line in _ascii:
        output = ""
        for char in line:
            if char in ['`', '$', '\\']:
                output += f"\\{char}"
            else:
                output += char
        write_to_file(file_name, output)

def main():
    file_name = get_filename()
    blank_slate(file_name)   
    proofer(file_name, ascii_art)

if __name__ == "__main__":
    main()
