input_1 = int(input("Give me a number"))

if input_1 > 1:
    for i in range(2, input_1):
        if(input_1 % i) == 0:
            print(input_1, "is not a prime number")
            break
    else:
        print(input_1, "is a prime number")
else:
    print(input_1, "is not a prime number")
