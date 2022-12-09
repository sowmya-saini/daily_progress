def sum_odd():
    num = int(input())
    sum_odd_num = 0
    num_digit = 1
    i = 0
    while(i != num):
        print(num_digit)
        sum_odd_num += num_digit
        num_digit += 2
        i += 1
    print(sum_odd_num)
    # for i in range(1, num +1):
    #     if i % 2:
    #         sum_odd_num += i
    # print(sum_odd_num)
sum_odd()
