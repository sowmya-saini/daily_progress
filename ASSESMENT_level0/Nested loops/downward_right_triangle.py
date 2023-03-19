def downward_right_triangle():
    number  = int(input())
    for i in range(number):
        for j in range(number-i):
            print("*", end=" ")
        print(" ")
downward_right_triangle()