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
    end=0
    while(i!=length):
        j += 1
        num = string_input[length-1-i:]
        if num.isdigit():
            number = int(num)
            print(num)
            if number  == length - j:
                end = number
            else:
                break
        else:
            break
        i += 1
    print(end)
    if end != 0:
        print(string_input[:end])
    else:
        print("The string is not valid")


removeMysteryL()

