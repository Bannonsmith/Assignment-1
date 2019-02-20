import json
user_input = ""
name = input("What is your name?")

with open("guest.json",'w') as file_object:
    json.dump(name,file_object)
responses = []
while user_input != "QUIT":
    user_input = input("Why do you like programming?")
    responses.append(user_input)

with open("guest.json",'a') as file_object:
    json.dump(responses,file_object)
