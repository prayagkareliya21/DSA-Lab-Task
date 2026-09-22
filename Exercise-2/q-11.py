# 11.	Write a function to find the maximum of three numbers.
def maximum(a, b, c):
    if a >= b and a >= c:
        return a;
    elif b >= a and b >= c:
        return b;
    else:
        return c;

num1 = float(input("Enter first number: "));
num2 = float(input("Enter second number: "));
num3 = float(input("Enter third number: "));

print("Maximum of three number is =", maximum(num1, num2, num3));