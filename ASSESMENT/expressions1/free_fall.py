import math
def freefall():
    distance = int(input())
    acceleration_due_g = 9.8
    final_speed = math.sqrt(2*acceleration_due_g*distance)
    print("Final speed is:", final_speed, "m/s")
freefall()
