def median_of_three(num1, num2, num3):
    if (num1<num2 and num1>num3) or (num1 > num2 and num1<num3):
        return num1
    elif (num2<num1 and num2>num3) or (num2 > num1 and num2<num3):
        return num2
    else:
        return num3
print(median_of_three(2, 7, 4))
print(median_of_three(2, 4, 7))
print(median_of_three(4, 2, 7))
print(median_of_three(4, 7, 2))
print(median_of_three(7, 2, 4))
print(median_of_three(7, 4, 2))

