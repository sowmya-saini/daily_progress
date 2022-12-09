def sandglass_pattern():
    number = int(input())
    for i in range(number):
        for space in range(i):
            print(" ", end = " ")
        for j in range(2*number - (2*i + 1)):
            if j % 2 == 0:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print(" ")
    for i in range(number):
        for s in range(number-i-1):
            print(" ", end = " ")
        for j in range(2 * i +1):
            if j % 2 == 0:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print(" ")
sandglass_pattern()