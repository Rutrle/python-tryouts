import csv
my_string = ''

with open('ex1.dat', newline='') as csvfile:
    for row in csvfile:
        for item in row:
            if item == ' ' or item.isdigit():
                my_string += item

print(my_string)


