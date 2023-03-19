def isCollinear(x1, y1, x2, y2, x3, y3):
    slope1 = (y2-y1)/(x2-x1)
    slope2 = (y3-y2)/(x3 - x2)
    slope3 = (y3-y1)/(x3 - x1)
    # print(slope1)
    # print(slope2)
    # print(slope3)
    if slope1 == slope2 or slope1 == slope3 or slope2 == slope3:
        return True
    else:
        return False
print(isCollinear(1, 4, 4, 6, 10, 10))