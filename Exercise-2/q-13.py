# 13.	Write a function to reverse a string.
def reverse_string(text):
    return text[::-1];

text = input("Enter a string: ");

print("Reversed string =", reverse_string(text));