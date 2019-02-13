
print("My name is Even Odd!")
print("I can tell if any number is even or odd!")
number1 = float(input("Give me a number!!!!ANY NUMBER!"))

def even_odd(number):
    if number % 2 == 0:
        print(number, "is Even")

    else:
        print(number, "is Odd")

print(even_odd(number1))




number = int(input("input number"))

if number % 2 == 0:
    print(number, "is even")

else:
    print(number, "is odd")
