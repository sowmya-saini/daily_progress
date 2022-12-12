import math
def getHypotenuse(side1 : int, side2:int) -> float:
    side3 = math.sqrt(side1 * side1 + side2 * side2)
    return side3

print(getHypotenuse(7, 8))