with open("learning.python.txt") as file_object:
  contents = file_object.read()
  print(contents.rstrip())

  for x in range(1):
    print(contents)

with open("learning.python.txt") as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line)
