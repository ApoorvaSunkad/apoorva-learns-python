# Take diameter of a circle as input from the user and calculate its area.
diameter = float(input("Please enter the diameter of the circle: "))
# Calculate the radius
radius = diameter / 2
# Calculate the area of the circle using the formula: Area = π * r^2
import math
area = math.pi * (radius ** 2)
# Print the area of the circle
print("The area of the circle with diameter", diameter, "is:", area)
