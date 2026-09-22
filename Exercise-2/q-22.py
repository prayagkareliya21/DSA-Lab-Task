# 22.	Write a function to find the second-largest number in a list.
def second_largest(numbers):
    largest = numbers[0]
    second = numbers[0]

    for number in numbers:
        if number > largest:
            second = largest
            largest = number
        elif number > second and number != largest:
            second = number

    return second


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = second_largest(numbers)

print("Second-largest number:", result)