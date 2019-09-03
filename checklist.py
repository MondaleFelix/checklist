checklist = []

# CREATE
def create(item):
    checklist.append(item)

 # READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    checklist[int(index)] = "{} {}".format("√", checklist[int(index)])

    # Add code here that marks an item as completed

def select(function_code):
    # Add item
    if function_code == "C" or function_code == "c":
        input_item = user_input("Add item: ")
        create(input_item)
        list_all_items()
    # Remove item
    elif function_code == "D" or function_code == "d":
        # remove from list
        if len(checklist) > 0:
            item_index = user_input("Enter index number: ")
            destroy(item_index)
            list_all_items()
        else: 
            print("Nothing to remove")

    # Update item with user input
    elif function_code == "U" or function_code == "u":
        item_index = user_input("Enter index number: ")
        input_item = user_input("Input Item: ")
        update(item_index, input_item)

    # Mark as complete
    elif function_code == "M" or function_code == "m":
        item_index = user_input("Enter index number: ")
        mark_completed(item_index)
        list_all_items()

    # Print all items
    elif function_code == "P" or function_code == "p":
        list_all_items()

    # Exit loop
    elif function_code == "Q" or function_code == "q":
        # This is where we want to stop our loop
        return False

    else:

        print("Invalid Input")
    return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input
    user_value = user_input("Please Enter a value: ")
    print(user_value)


# def test():
#     # Your testing code here
#     # ...
#     # Call your new function with the appropriate value
#     # select("C")
#     # View the results
#     # list_all_items()
#     # Call function with new value
#     # select("R")
#     # View results
#     # list_all_items()
#     # Continue until all code is run
#     # list_all_items()



running = True
while running:
    selection = user_input(
        "Press C to Add to list, D to Remove from list, U to Update item, M to mark as Complete, and P to Show list. Press Q to Quit. ")
    running = select(selection)
