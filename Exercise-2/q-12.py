# 12.	Write a function to count vowels in a string.
def count_vowels(text):
    count = 0;

    for char in text:
        if char.lower() in "aeiou":
            count += 1;

    return count;

text = input("Enter a string: ");

print("Number of vowels =", count_vowels(text));

