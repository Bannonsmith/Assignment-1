class User:
    def __init__(self,  first_name, lat_name, age, active):
        self.first_name = first_name
        self.lat_name   = lat_name
        self.age        = age
        self.active     = active


    def greet(self):
        print(f"Good day, {self.first_name} {self.lat_name}, and your age is {self.age} and your {self.active}")

    def describe_user(self):
        print(f"{self.first_name} + {self.lat_name} + {self.age} + {self.active}")


user = User("john", "doe", 17, "active")
user.greet()
user.describe_user()
