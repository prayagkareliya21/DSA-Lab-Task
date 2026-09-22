# 20.	Write a function to return all prime numbers between two numbers.

def prime_numbers(start, end):
    primes = []

    for number in range(start, end + 1):
        if number > 1:
            is_prime = True

            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break

            if is_prime:
                primes.append(number)

    return primes


start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

result = prime_numbers(start, end)

print("Prime numbers:", result)