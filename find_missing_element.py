numbers =[0, 1, 3, 4, 5, 6, 7, 8, 9]

def find_missing_number(numbers):
        answer = 45 - sum(numbers)
        return answer
print(find_missing_number(numbers) )
