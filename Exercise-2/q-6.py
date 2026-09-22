# 6.	Write a function to find the maximum of two numbers.
def maximum(a, b):
    if a > b:
        return a;
    else:
        return b;

num1 = int(input("Enter first number: "));
num2 = int(input("Enter second number: "));

print("Maximum of two number is =", maximum(num1, num2));
