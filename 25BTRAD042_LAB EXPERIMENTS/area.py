import math

# Area of Rectangle
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

rect_area = length * width
print(f"Area of Rectangle: {rect_area}")

# Area of Circle
radius = float(input("Enter radius of circle: "))

circle_area = math.pi * (radius ** 2)
print(f"Area of Circle: {circle_area:.2f}")