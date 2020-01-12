import sys
import csv

file_name = sys.argv[1]
argument = sys.argv[2]

with open("unified/" + file_name, newline= '') as csvfile:
    reader = csv.DictReader(csvfile)
    origin = []
    count = 0
    for row in reader:
        if row[argument] not in origin:
            origin.append(row[argument])
            count = count + 1

print (origin)
print (count)
