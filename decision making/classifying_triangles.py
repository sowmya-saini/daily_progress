def classifying_triangles():
    side1 = int(input())
    side2 = int(input())
    side3 = int(input())
    if side1 == side2 and side2 == side3:
        print("The triangle is equilateral")
    elif side1 != side2 and side1!= side3 and side2 != side3:
        print("The triangle is scalene")
    else:
        print("The triangle is iosceles")
classifying_triangles()