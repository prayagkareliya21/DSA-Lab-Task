# 18.	Write a function to count how many times an element appears in a list.
def count_element(lst, element):
    count = 0

    for item in lst:
        if item == element:
            count += 1

    return count


numbers = list(map(int, input("Enter elements separated by spaces: ").split()));

element = int(input("Enter the element you want to count: "));

result = count_element(numbers, element);

print("Element", element, "appears", result, "times");