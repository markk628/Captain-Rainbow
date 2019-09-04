#integer = len()

checklist = list()


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
    for index, list_item in enumerate(checklist):
        print(str(index) + list_item)
        index += 1

def mark_completed(index):
    update(index, " √ " + checklist[index])


def select(function_code):
    try:
        # Create item
        if function_code.upper() == "C":
            input_item = user_input("Input item: ")
            create(input_item)
            return True

        # Read item
        elif function_code.upper() == "R":
            item_index = int(user_input("Index Number?: "))
            if item_index > len(checklist):
                print("Try another number")
            #elif item_index = str(user_input("Index Number?"))
                #print("Enter a number please")
            else:
                # Remember that item_index must actually exist or our program will crash.
                value = read(item_index)
                print (value)
            return True

         # Print all items
        elif function_code.upper() == "P":
            list_all_items()
            return True

        elif function_code.upper() == "Q":
        # This is where we want to stop our loop
            return False

        elif function_code.upper() == "U":
            item_index = int(user_input("Index Number: "))
            item_update = user_input("What you want fam: ")
            update(item_index, item_update)
            return True

        elif function_code.upper() == "D":
            item_index = int(user_input("Index Number: "))
            destroy(item_index)
            return True

        elif function_code.upper() == "M":
            item_index = int(user_input("Index Number: "))
            mark_completed(int(item_index))
            return True

        # Catch all
        else:
            print("Unknown Option")
            return True
    except:
        print("invalid input")
        return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def test():
    #create("purple sox")
    #create("red cloak")

    #print(read(0))
    #print(read(1))

    #update(0, "purple socks")
    #destroy(1)

    #print(read(0))

    select("C")
    list_all_items()

    select("R")
    list_all_items()

    select("P")
    list_all_items()

    select("Q")
    list_all_items()

    user_value = user_input("Please Enter a value:")
    print(user_value)

#test()


if __name__ == "__main__":

    running = True
    while running:
        selection = user_input(
            "Press C to add to list, R to Read from list, P to display list, U to update an item, D to delete an item, M to mark complete, and Q to quit: ")
        running = select(selection)
