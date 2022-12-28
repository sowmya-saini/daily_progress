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
    terminate = 0
    no_of_flips = 0
    while(terminate != 1):
        num = head_or_tail()
        # print(num)
        no_of_flips += 1
        # print("no of flips",no_of_flips)
        if (head == "Head" and num == 0) or (tail == "Tail" and num == 1):
            terminate = 1
        if num == 0:
            head = "Head"
            tail = ""
        else:
            tail = "Tail"
            head = ""
    return no_of_flips
getNumOfFlips()

def resultant_flips():
    minimum = 0
    maximum = 0
    Average = 0
    for i in range(10):
        no_of_flips = getNumOfFlips()
        Average += no_of_flips
        print(no_of_flips)
        if minimum == 0 or minimum > no_of_flips:
            minimum = no_of_flips
        elif maximum == 0 or maximum <no_of_flips:
            maximum = no_of_flips
    print("Minimum number of flips :",minimum)
    print("Maximum number of flips :", maximum)
    print("Average number of flips :",Average//10)
   
resultant_flips()