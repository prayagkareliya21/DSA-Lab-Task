# 7. Create a simple calculator using if-elif-else.
num1 = float(input("Enter first number: "));
operator = input("Enter operator (+, -, *, /): ");
num2 = float(input("Enter second number: "));

if operator == "+":
    print("\nResult:", num1 + num2);
elif operator == "-":
    print("\nResult:", num1 - num2);
elif operator == "*":
    print("\nResult:", num1 * num2);
elif operator == "/":
    if num2 != 0:
        print("\nResult:", num1 / num2);
    else:
        print("\nCannot divide by zero");
else:
    print("\nInvalid operator");

