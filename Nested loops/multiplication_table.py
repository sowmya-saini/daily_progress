def multiplication_table():
    rows = 11
    col = 11
    for i in range(rows):
        if i == 0:
            print("{:5}".format(" "), end = " ")
        else:
            print("{:5d}".format(i), end = " ")
        for j in range(1,col):
            if i == 0:
                print("{:5d}".format(j), end = " ")
            else:
                print("{:5d}".format(i*j), end= " ")
        print("")
multiplication_table()