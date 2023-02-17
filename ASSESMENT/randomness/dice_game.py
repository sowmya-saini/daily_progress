import random as r
def DiceGame():
    count = 0
    for i in range(10):
        num = r.randint(1, 6)
        # print(num)
        if num == 6:
            count += 1
    return count
print(DiceGame())