names = ["Alex", "John", "Mary", "Steve", "John", "Steve"]

def remove_duplicates(names):
    new_list = []
    for name in names:
        if name not in new_list:
            new_list.append(name)
    return new_list


print(remove_duplicates(names))
