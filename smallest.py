elements = [45, 46, -1, 50, 1002, 35, 10]
def smallest_element(elements):
    small = 0
    for element in elements:
        if element < small:
            small = element
    return small
print(smallest_element(elements))
