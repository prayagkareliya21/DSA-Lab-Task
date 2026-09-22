# 15.	Write a function to find the sum of all elements in a list.
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [10, 20, 30, 40, 50]
print(sum_list(numbers)) 
