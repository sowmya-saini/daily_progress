def sum_of_digits():
    num = int(input("Enter the integer: "))
    # str_num = list(str(num))
    # digits = [int(i) for i in str_num]
    # print(sum(digits))

    sum_all_digits = 0
    reminder = num % 10
    num = num // 10
    sum_all_digits += reminder

    reminder = num % 10
    num = num // 10
    sum_all_digits += reminder

    reminder = num % 10
    num = num // 10
    sum_all_digits += reminder

    reminder = num % 10
    num = num // 10
    sum_all_digits += reminder

    print("sum of all 4 digits :",sum_all_digits)

sum_of_digits()