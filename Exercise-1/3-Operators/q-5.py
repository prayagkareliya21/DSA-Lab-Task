# 5. Demonstrate logical operators (and, or, not).

a = int(input("\nEnter first number: "));
b = int(input("Enter second number: "));

# True only when both conditions are True.
print("\na > 0 and b > 0:", a > 0 and b > 0);

# True when at least one condition is True.
print("a > 100 or b > 100:", a > 100 or b > 100);

# Reverses the result (True → False, False → True).
print("not(a > 0):", not(a > 0));
