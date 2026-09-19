# 4. Check whether a year is a leap year.
year = int(input("Enter a year: "));

if year % 400 == 0:
    print("\nLeap year");
elif year % 100 == 0:
    print("\nNot a leap year");
elif year % 4 == 0:
    print("\nLeap year");
else:
    print("\nNot a leap year");
