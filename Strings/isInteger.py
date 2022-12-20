def isInteger(string_input):
    without_spaces = string_input.replace(' ', '')
    print(without_spaces)
    validInteger = 0
    for i in range(len(without_spaces)):
        if i==0 and (without_spaces[i] == '+' or without_spaces[i] == '-'):
            validInteger = 0
        elif without_spaces[i].isdigit():
            validInteger = 0
        else:
            validInteger = 1
            break
    if validInteger == 0:
        return "Given string represents valid Integer"
    else:
        return "Given string is not a valid Integer"


print(isInteger(" 1 2 + 4 5"))
print(isInteger(" + 1 2 + 4 5"))
print(isInteger(" - +  2 4 5"))
print(isInteger(" +    1 2  4 5"))
print(isInteger(" - 1 2  4 5"))
print(isInteger(" 1 2 4 5"))
print(isInteger(" 1 2  4 5 - "))







