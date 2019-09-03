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
    checklist[index] = "{} {}".format("√", checklist[index])

    # Add code here that marks an item as completed

def test():
