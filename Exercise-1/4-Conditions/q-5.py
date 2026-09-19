# 5. Create a grade system based on marks. 
name = str(input("Enter your name: "));
marks = int(input("Enter your marks: "));

print("\n")

if marks >= 90:
    print(name," got Grade A");
elif marks >= 80:
    print(name," got Grade B");
elif marks >= 70:
    print(name," got Grade C");
elif marks >= 60:
    print(name," got Grade D");
elif marks >= 50:
    print(name," got Grade E");
else:
    print(name, "Fail exam");
