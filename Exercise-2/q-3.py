# 3.	Write a function to add two numbers.
a = int(input("Enter first number: "));
b = int(input("Enter second number: "));

def add(a, b):
    addition = a + b;
    return addition;

result = add(a, b)
print("Addition of two number: ",result);
