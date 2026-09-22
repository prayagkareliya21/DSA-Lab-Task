# 14.	Write a function to check whether a string is a palindrome.
def is_palindrome(string):
    return string == string[::-1];


# Example
string = input("Enter a string: ")

if is_palindrome(string):
    print("Palindrome")
else:
    print("Not a palindrome")
