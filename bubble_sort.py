def bubbleSort(list):
    for i in range (0,len(list) -1):
        for j in range(0, len(list) - 1 - i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

list = [2,55,6,969,13,1000]
print(bubbleSort(list))
