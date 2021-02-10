# checks if something is valid

import re

data = ["A", "B", "C"]

has_errors = "yes"
while has_errors == "yes":

    filename = input("Enter a filename: ")
    has_errors = "no"

    valid_char = "[A-Za-z0-9_]"
    for i in filename:
        if re.match(valid_char, i):
            continue

        elif i == " ":
            problem = "(no spaces allowed)"

        else:
            problem = ("no {}'s allowed".format(i))

        has_errors = "yes"


    if filename == "":
        problem = "can't be blank"
        has_errors = "yes"

    if has_errors == "yes":
        print("Invalid filename - {}".format(problem))

    else:
        print("You entered a valid filename")

filename += ".txt"

f = open(filename, "w+")

for i in data:
    f.write(i + "\n")

f.close()
