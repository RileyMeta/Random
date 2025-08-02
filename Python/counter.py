import os
import argparse
import sys

FILE = "./counter.txt"

def get_counter(file: str):
    """ Parse FILE for current counter int """
    try:
        with open(file, 'r') as f:
            counter = f.readline().strip()
            return int(counter)
    except (ValueError, FileNotFoundError):
        counter = 1
        return counter

def write_to_file(counter: int):
    """ Overwrite the file with the current counter """
    try:
        with open(FILE, 'w') as f:
            f.write(str(counter))
    except Exception as e:
        print(f"Error writing to file: {e}")

def increment_counter(counter: int, step: int = 1):
    """ increment the COUNTER by STEP or 1 if none """
    write_to_file(counter + step)

def decrement_counter(counter: int, step: int = 1):
    """ decrement the COUNTER by STEP or 1 if none """
    write_to_file(counter - step)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple increment / decrement program.")
    parser.add_argument("-i", "--increment", action="store_true", help="Increase the counter by a specific amount.")
    parser.add_argument("-d", "--decrement", action="store_true", help="Decrease the counter by a specific amount.")
    parser.add_argument("-c", "--custom", type=int, default=1, help="Set a custom step for the counter.")

    args = parser.parse_args()

    counter = get_counter(FILE)

    if args.increment:
        increment_counter(counter, args.custom)
    elif args.decrement:
        decrement_counter(counter, args.custom)
    else:
        increment_counter(counter)
