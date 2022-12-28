def removeMysteryL():
    string_input = input()
    length = len(string_input)
    i=0
    
    # while(i!=length):
    #     print(string_input[length - 1-i:])
    #     i+=1


    # while(i!=length):
    #     num = string_input[length-1-i:]
    #     if num.isdigit():
    #         num = int(num)
    #         print(num)
    #     else:
    #         break
    #     i += 1


    # while(i!=length):
    #     num = string_input[length-1-i:]
    #     if num.isdigit():
    #         num = int(num)
    #         print(num)
    #     else:
    #         break
    #     i += 1
    j=0
    while(i!=length):
        j += 1
        num = string_input[length-1-i:]
        if num.isdigit():
            number = int(num)
            print(num)
            if number  <= length - j:
                end = number
            else:
                break
        else:
            break
        i += 1
    print(end)
    print(string_input[:end])


removeMysteryL()


# def removeMysteryLength(string_input):
#     length = len(string_input)
#     number = ""
#     i=0
#     num = 0
#     while(num < length):
#         number = string_input[length - i - 1:]
#         num = int(number)
#         i += 1
    
#     l = string_input[length-len(number) + 1:]
#     return string_input[:int(l)]
# print(removeMysteryLength("sainiSowmya25"))
# print(removeMysteryLength("JamesBond00712"))
# print(removeMysteryLength("sjhdkjkjkdsksdkjsdl1jhh122"))
