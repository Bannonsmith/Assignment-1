elements = [32, 45, 25, 56, 10, 1]
def largest_element(elements):
    largest = 0
    for element in elements:
        if element > largest:
            largest = element
    return largest
print(largest_element(elements))
