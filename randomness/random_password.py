import random
def randomPassword():
    password_generated = ""
    length = random.randint(7, 10)
    # print(length)
    for i in range(length):
        asciinum = random.randint(33, 126)
        password_generated += chr(asciinum)
    return password_generated
print(randomPassword())