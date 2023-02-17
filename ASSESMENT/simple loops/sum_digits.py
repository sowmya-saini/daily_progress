def sum_digits():
    number = int(input())
    string_in = str(number)
    int_string = [int(i) for i in string_in]

    # print(sum(int_string))

    sum_all =0 
    for i in range(len(int_string)):
        sum_all += int_string[i]
    print(sum_all)
sum_digits()
