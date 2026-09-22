# 10.	Write a function to check whether a number is positive, negative, or zero.
def check_number(num):
    if num > 0:
        return "Positive";
    elif num < 0:
        return "Negative";
    else:
        return "Zero";

num = float(input("Enter a number: "));

print(check_number(num));