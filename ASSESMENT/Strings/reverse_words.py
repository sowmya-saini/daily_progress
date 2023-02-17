def reverseWords():
    words = input()
    splitting = words.split(" ")
    string_result = ""
    i = len(splitting)
    while(i !=0):
        string_result += splitting[i-1]
        string_result += " "
        i -= 1
    return string_result
print(reverseWords())

