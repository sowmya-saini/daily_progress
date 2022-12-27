import random as r
def head_or_tail():
    head_tail = r.randint(0, 1)
    if head_tail == 0:
        return 0
    else:
        return 1

def getNumOfFlips():
    head = ""
    tail = ""
    no_of_flips = 0
    for i in range(10):
        num = head_or_tail()
        print(num)
        no_of_flips += 1
        print("no of flips",no_of_flips)
        if (head == "Head" and num == 0) or (tail == "Tail" and num == 1):
            break
        if num == 0:
            head = "Head"
            tail = ""
        else:
            tail = "Tail"
            head = ""
    return no_of_flips
getNumOfFlips()

# def resultant_flips():
#     no_of_flips = getNumOfFlips()
#     return no_of_flips
# print(resultant_flips())