def is_valid_triangle(side1 : int, side2 : int, side3 : int)->bool:
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return False
    elif side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2:
        return False
    else:
        return True
print(is_valid_triangle(7, 5, 10))

#taking external input

def is_valid_triangle():
    side1 = int(input())
    side2 = int(input())
    side3 = int(input())
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return False
    elif side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2:
        return False
    else:
        return True
print(is_valid_triangle())

