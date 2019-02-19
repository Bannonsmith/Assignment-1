user_input = ""
print("Grocery App")
# Ask user for the input
#input_1 = input("Which store would you like to go to?")
#input_2 = input("brief description")
#Create shopping list- with title and description
user_input = ""
store_list = []
total = 0

class Grocery:
    def __init__(self, name, quantity, price, total):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.total = total



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
    view_shopping_list()
    store_list_number = int(input("Enter shopping list number to add the grocery item: "))
    store_lists = store_list[store_list_number - 1]
    name = input("What item would you like to add  ")
    quantity = float(input("How many {} would you like  ".format(name)))
    price = float(input("What is the price?  "))
    total = quantity * price
    grocery = Grocery(name,quantity,price,total)
    store_lists.grocery_items.append(grocery)


def view_shopping_list():
    for index in range(0,len(store_list)):
        store = store_list[index]
        print(f"{index + 1} - {store.name} - {store.description}")
        for grocery in store.grocery_items:
            print(f"item - {grocery.name} quantity-{grocery.quantity} each worth ${grocery.price}")
            print(f"Your total cost for those item/items:  {grocery.total}")
            for i in range(float(grocery.total)):
                sum += i
                print(f"Your final bill: {sum}")


#store_list = StoreList(store, description, grocery)
#grocery = Grocery(name, quantity, price)

show_menu()

try:
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
except ValueError:
    print("Please input from the selection above")

# The user shoule be able to add multiple shopping list
# Give user option to display that list
# User can add a grocery item to list- with title
# use format in schoology to print it out
