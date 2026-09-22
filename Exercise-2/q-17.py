# 17.	Write a function to remove duplicate elements from a list.
def remove_duplicates(lst):
    return list(set(lst));

numbers = [1, 2, 3, 2, 4, 1, 5, 6, 7, 8, 6, 9, 11, 5, 6];

result = remove_duplicates(numbers);

print("List after removing duplicates:", result);