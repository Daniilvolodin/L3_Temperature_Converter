# data outputted
data = ['first', 'second', 'third', 'fourth', 'fifth', "sixth", "seventh"]

# Get filename, can't be blank / invalid
# assume valid data for now.
filename = input("Enter a filename: ")

# add.txt suffix
filename += ".txt"

# create file to hold data
f = open(filename, "w+")

# add new line at end of each item
for i in data:
    f.write(i + "\n")

# close file
f.close()