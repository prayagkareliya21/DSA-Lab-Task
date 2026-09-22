# 16.	Write a function to find the largest element in a list.
def largest_element(numbers):
    largest = numbers[0];

    for num in numbers:
        if num > largest:
            largest = num;

    return largest;


numbers = list(map(int, input("Enter numbers: ").split()));

print("Largest element =", largest_element(numbers));
