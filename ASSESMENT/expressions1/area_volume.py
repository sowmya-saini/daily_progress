import math
def area_volume():
    radius = float(input("Enter the radius is:"))
    area_circle = math.pi * radius * radius
    volume_sphere = (4/3) * math.pi * radius * radius * radius
    print("Area of circle is:", area_circle)
    print("Volume of sphere is:", volume_sphere)
area_volume()