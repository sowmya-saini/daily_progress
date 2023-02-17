import math
def area_triangle():
    side1 = int(input("Enter side1: "))
    side2 = int(input("Enter side2: "))
    side3 = int(input("Enter side3: "))
    s = (side1 + side2 + side3)/2
    # print(s)
    s1 = s*(s-side1)*(s-side2)*(s-side3)
    # print(s1)
    area = math.sqrt(s1)
    print("The area of triangle is", area)
area_triangle()