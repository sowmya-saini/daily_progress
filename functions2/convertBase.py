def anybase_to_baseten(num, base1):
    num = str(num)
    length = len(num)
    pow_len = length-1
    sum_all_digits = 0
    for i in range(len(num)):
        if num[i]== "A":
            digit = 10
        elif num[i] == "B":
            digit == 11
        elif num[i] == "C":
            digit == 12
        elif num[i] == "D":
            digit == 13
        elif num[i] == "E":
            digit == 14
        elif num[i] == "F":
            digit == 15
        else:
            digit = int(num[i])
        sum_all_digits += digit * base1 ** pow_len
        pow_len -= 1
    return sum_all_digits
# anybase_to_baseten("6AF", 5)

def baseten_to_desired_base(num, base2):
    required = ""
    while(num >= base2):
        rem = num % base2
        if rem >= 15:
            required += chr(87 + rem)
        else:
            # rem1= str(rem)
            required += str(rem)
        num = num // base2
        if num < base2:
            required += str(num)
    reverse = ""
    i = len(required)-1
    while(i != -1):
        reverse += required[i]
        i -= 1
    return reverse
# print(baseten_to_desired_base(2345, 12))


def anybase_converter(number, base1, base2):
    if base1 >=2 and base1 <= 16 and base2 >= 2 and base2 <= 16:
        base_ten = anybase_to_baseten(number, base1)
        return baseten_to_desired_base(base_ten, base2)
    else:
        return "Enter valid bases"

print(anybase_converter(10011, 2, 16))