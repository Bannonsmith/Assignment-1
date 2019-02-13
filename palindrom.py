print("I am an application that will check and see if your word is a Palindrom.")

input_1 = input(("Enter a single word"))

input_lowercase = input_1.casefold()

rev_input = input_lowercase[::-1]

if input_lowercase == rev_input:
    print("It is a palindrom")
else:
    print("It is not a palindrom")
