def greet():
    return ("Welcome to the Calculator App- your very limited calc app")
print(greet())

input_1 = float(input("What is your first number? "))
input_2 = input("What do you want to do with that number? (ie. +,-,*,/) ")
input_3 = float(input("Give me one last number that will affect that first number you entered "))

def operator(one, two, three):
    if two == "+":
        answer = (one) + (three)
        return (answer)
    elif two == "-":
        answer = (one) - (three)
        return (answer)
    elif two == "*":
        answer = (one) * (three)
        return (answer)
    elif two == "/":
        answer = (one) / (three)
        return (answer)
    else:
        return("You must use either (+,-,*,/) for me to function")

print(operator(input_1, input_2, input_3
