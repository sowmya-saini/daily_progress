import random
def rollDice():
    ones = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    for i in range(5):
        num = random.randint(1, 6)
        if num == 1:
            ones += 1
        elif num == 2:
            two += 1
        elif num == 3:
            three += 1
        elif num == 4:
            four += 1
        elif num == 5:
            five += 1
        else:
            six += 1
        print(num)  
    if ones == 5 or two == 5 or three == 5 or four  == 5 or five == 5 or six == 5:
        return "Yahooo!!!"
    else:
        return "TRY AGAIN..."
print(rollDice())


def rollDice():
    no_on_dice = []
    for i in range(5):
        num = random.randint(1, 6)
        no_on_dice.append(num)
    boolval = all(i == no_on_dice[0] for i in no_on_dice)
    print(no_on_dice)
    if boolval == True:
        return "Yahooo!!!"
    else:
        return "Try Again.."
print(rollDice())