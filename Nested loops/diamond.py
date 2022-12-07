def diamond():
    number = int(input())
    num = number-1
    for i in range(number):
        for space in range(number - i- 1):
            print(" ", end = " ")
        for j in range(2 * i+ 1):
            print("*", end = " ")
        print(" ")
    for i in range(num):
        for space in range(i+1):
            print(" ", end = " ")
        for j in range(2*num - (2*i+1)):
            print("*", end = " " )
        print(" ")
diamond()
