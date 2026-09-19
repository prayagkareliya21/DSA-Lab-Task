# 2. Swap the values of two variables.

a = int(input("Enter number one: "));
b = int(input("Enter number two: "));

print("\nBefore swaping the number : ");
print("Here is first number ", a);
print("Here is second number ", b);

temp = a;
a = b;
b = temp;

print("\nAfter swaping the number : ");
print("Here is first number ", a);
print("Here is second number ", b);
