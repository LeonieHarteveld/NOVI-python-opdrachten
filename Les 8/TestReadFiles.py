import sys

try:
    with open("test.txt", 'r') as file:
        print(file.read())
except FileNotFoundError:
    print(f"That file was not found", file=sys.stderr)