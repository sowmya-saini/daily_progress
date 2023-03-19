def decimal_to_binary():
    decimal_num = int(input())

    #inbuilt 
    bin_num = bin(decimal_num)
    print(bin_num[2:])
    #actual
    string_bin =""
    while(decimal_num != 1):
        num = decimal_num
        decimal_num = decimal_num //2
        if num - decimal_num *2== 0:
            string_bin += "0"
        else:
            string_bin += "1"
    string_bin += "1"
    reverse_bin = ""
    i = len(string_bin)-1
    while(i != -1):
        reverse_bin += string_bin[i]
        i -= 1
    print(reverse_bin)
   
decimal_to_binary()

    

