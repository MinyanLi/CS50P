import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]
splitfilename = filename.split(".")
filetype = splitfilename[-1]

if filetype != "py":
    sys.exit("Not a Python file")

n = 0
try:
    with open(filename) as file:
        for line in file:
            if line.strip() != "" and line.strip().startswith("#") == False:
                n += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(n)