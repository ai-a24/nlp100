import sys

def readlines_file(name):
    with open(name, 'r') as file:
        return file.readlines()

lines = readlines_file(sys.argv[1])

n = sys.argv[2]

print("".join(lines[::int(n)]))
