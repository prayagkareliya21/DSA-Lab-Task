# 24.	Write a function to merge two lists and remove duplicates.

def merge_lists(list1, list2):
    result = []

    for item in list1:
        if item not in result:
            result.append(item)

    for item in list2:
        if item not in result:
            result.append(item)

    return result


list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

result = merge_lists(list1, list2)

print("Merged list without duplicates:", result)