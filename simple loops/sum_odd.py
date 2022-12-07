def sum_odd():
    num = int(input())
    sum_odd_num = 0
    for i in range(1, num +1):
        if i % 2:
            sum_odd_num += i
    print(sum_odd_num)
sum_odd()
