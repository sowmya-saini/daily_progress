def removeMysteryLength(string_input):
    length = len(string_input)
    number = ""
    i=0
    num = 0
    while(num < length):
        number = string_input[length - i - 1:] 
        num = int(number)
        i += 1
    l = string_input[length-len(number) + 1:]
    return string_input[:int(l)]
print(removeMysteryLength("sainiSowmya25"))
print(removeMysteryLength("JamesBond00712"))
print(removeMysteryLength("sjhdkjkjkdsksdkjsdl1jhh122"))