def inverted_pyramid():
    number = int(input())
    for i in range(number):
        for space in range(i):
            print(" ", end = " ")
        for j in range(2*number - (2*i + 1)):
            print("*", end = " ")
        print(" ")
inverted_pyramid()