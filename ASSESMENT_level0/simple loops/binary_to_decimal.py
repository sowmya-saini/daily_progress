
def binary_to_decimal():
    binary_num = input()
    length = len(binary_num)
    for_two = length-1
    sum_all_digits = 0
    for i in range(len(binary_num)):
        bin_digit = int(binary_num[i])
        sum_all_digits += bin_digit * 2 ** for_two
        for_two -= 1
    print(sum_all_digits)
    #by inbuilt function
    print(int(binary_num, 2))
binary_to_decimal()


