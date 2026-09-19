# 4. Calculate simple interest using variables.

amount = 10000;
rate = 15;
time = 5;

print("The main amount is", amount,"$"); 
print("Rate of interest is",rate,"%"); 
print("duration for pay back the amount in", time, "month.");

interest = (amount * rate * time) / 100;

print("Here is the the simple interest for the given amount, rate and time is", interest,"$");

print("The total amount after interest after adding interest amount to the main amount is", (amount + interest), "$");