def removeMysteryLength(string_input, length):
    string_res = ""
    i = 0
    while(len(string_res) != length):
        string_res += string_input[i]
        i+=1
    return string_res
print(removeMysteryLength("sainiSowmya25", 10))