all_calculations = []

get_item = ""

while get_item != "xxx":
    get_item = input("Enter an Item")

    if get_item == "xxx":
        break

    all_calculations.append(get_item)

if len(all_calculations) == 0:
    print("The list is empty")

else:

    print("**** The Full list ****")
    print(all_calculations)

    if len(all_calculations) >= 3:
        print("**** Most Recent 3 ****")
        for i in range(0,3):
            print(all_calculations[len(all_calculations) - i - 1])

    else:
        print("**** Items from newest to oldest ****")
        for i in all_calculations:
            print(all_calculations[len(all_calculations) - all_calculations.index(i)])
