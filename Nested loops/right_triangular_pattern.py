def right_triangular_pattern():
    n = int(input())
    for i in range(n):
        for j in range(i+1):
            print("*", end = " ")
        print(" ")
right_triangular_pattern()