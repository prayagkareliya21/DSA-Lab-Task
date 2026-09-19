# 2. Check whether a person is eligible to vote.
nm = str(input("Enter your name: "));
age = int(input("Enter your age: "));

if age >= 18:
    print(nm, "Eligible to vote.");
else:
    print(nm, "Not eligible to vote."); 