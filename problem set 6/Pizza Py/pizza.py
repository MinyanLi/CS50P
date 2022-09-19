import sys
from tabulate import tabulate
import csv

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]
splitfilename = filename.split(".")
filetype = splitfilename[-1]

if filetype != "csv":
    sys.exit("Not a CSV file")

pizzas = []
try:
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            pizzas.append(row)
except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(pizzas,  headers = "firstrow", tablefmt="grid"))
