

n = int(input("Give me a number"))
def fact(new):
    f = 1
    for index in range(1, new+1):
        f = f * index
    return f

print(fact(n))
