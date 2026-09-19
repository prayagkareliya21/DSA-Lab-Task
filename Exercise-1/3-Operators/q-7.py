# 7. Find the largest of two numbers using comparison operators.
num1 = int(input("\nEnter first number: "));
num2 = int(input("Enter second number: "));

if num1 > num2:
    print("\nLargest number is:", num1);
elif num2 > num1:
    print("\nLargest number is:", num2);
else:
    print("\nBoth numbers are equal.");
