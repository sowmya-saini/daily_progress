import random as r

def randomLicensePlate():

    new_or_old = r.randint(0, 1)
    print(new_or_old)
    if new_or_old == 0:
        return old_licensePlate()
    else:
        return newLicensePlate()


def old_licensePlate():
    old = ""
    for i in range(3):
        character = r.randint(65, 122)
        old += chr(character)
    for i in range(3):
        old += str(r.randint(0, 9))
    return old



def newLicensePlate():
    new = ""
    for i in range(4):
        new += str(r.randint(0, 9))
    for i in range(3):
        character = r.randint(65, 122)
        new += chr(character)
    return new






print(randomLicensePlate())
