class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.name + ' - ' + self.cuisine_type)

    def open_restaurant(self):
        print("Resturant is open")



restaurant = Restaurant("Jimmy's BBQ","BBQ")
restaurant2 = Restaurant("Olive Garden", "Italian")
restaurant3 = Restaurant("McDonald's", "Fast Food")
print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant.open_restaurant()
