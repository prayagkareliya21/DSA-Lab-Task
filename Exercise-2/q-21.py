# 21.	Write a function to calculate Fibonacci numbers.
def fibonacci(n):
    a = 0
    b = 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result


n = int(input("Enter how many Fibonacci numbers you want: "))

print("Fibonacci numbers:", fibonacci(n))