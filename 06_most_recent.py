# Get data from user and store it in a list,
# then display the most recent three entries nicely

# Set up empty list
all_calculations = []

# Get five items of data
for i in range(0,5):
    get_item = input("Enter an item")
    all_calculations.append(get_item)


# Show that everything made it to the list...
print('\n**** The Full List ****')
print(all_calculations, '\n')
print("**** Most Recent 3 ****")
# print items starting at the end of the list
for x in range(0, 3):
    print(all_calculations[len(all_calculations) - x - 1])