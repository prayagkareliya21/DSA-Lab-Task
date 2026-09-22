# 23.	Write a function to sort a list without using sort().

def sort_list(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = sort_list(numbers)

print("Sorted list:", result)