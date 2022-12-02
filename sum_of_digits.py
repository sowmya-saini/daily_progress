def sum_of_digits():
    num = int(input("Enter the integer: "))
    str_num = list(str(num))
    digits = [int(i) for i in str_num]
    print(sum(digits))
sum_of_digits()