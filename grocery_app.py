user_input = ""
print("Grocery App")
# Ask user for the input
#input_1 = input("Which store would you like to go to?")
#input_2 = input("brief description")
#Create shopping list- with title and description
user_input = ""
store_list = []
grocery_list = []

class Grocery:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price



class StoreList:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.grocery_items = []


def show_menu():
    print("Press 1 to add new shopping list")
    print("Press 2 to delete shopping list")
    print("Press 3 to view all shopping list")
    print("Press 4 to add to grocery item to shopping list")
    print("Print q to quit")



def add_shopping_list():
    name = input("Which store would you like to go to?  ")
    description = input("brief description  ")
    store = StoreList(name,description)
    store_list.append(store)
    show_menu()

def add_grocery_item():
    name = input("What item would you like to add  ")
    quantity = input("How many {} would you like  ".format(name))
    price = input("What is the price?  ")
    for index in range(0,len(store_list)):
        stores = store_list[index]
        print(f"{index + 1} - {stores}")
        #grocery = Grocery(name,quantity,price)
        #grocery_list.append(grocery)
        #show_menu()

def view_shopping_list():
    for store in store_list:
        print("{} - {}".format(store.name,store.description))
    for grocery in grocery_list:
        print("item{} q{} each worth ${}".format(grocery.name,grocery.quantity,grocery.price))

#store_list = StoreList(store, description, grocery)
#grocery = Grocery(name, quantity, price)

show_menu()

all_list = []
while user_input != "q":
    user_input = input("Enter your choice:  ")

    if user_input == "1":
        add_shopping_list()
    elif user_input == "2":
        delete_shopping_list()
    elif user_input == "3":
        view_shopping_list()
    elif user_input == "4":
        add_grocery_item()


# The user shoule be able to add multiple shopping list
# Give user option to display that list
# User can add a grocery item to list- with title
# use format in schoology to print it out
