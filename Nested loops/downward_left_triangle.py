def downward_left_triangle():
    number = int(input())
    for i in range(number):
        for space in range(i):
            print(" ", end = " ")
        for j in range(number-i):
            print("*", end = " ")
        print(" ")
downward_left_triangle()