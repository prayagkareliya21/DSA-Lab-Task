# 8.	Write a function to calculate the area of a circle.
def area_of_circle(radius):
    return 3.14 * radius * radius;

radius = float(input("Enter radius of the circle: "));

area = area_of_circle(radius);

print("Area of circle =", area);