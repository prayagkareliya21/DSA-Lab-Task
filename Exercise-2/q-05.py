# 5.	Write a function to check whether a number is even or odd.
def checker(n):
    if n % 2 == 0:
        return "Even";
    else:
        return "Odd";

number = int(input("Enter the number "));
print("Your number is",checker(number));