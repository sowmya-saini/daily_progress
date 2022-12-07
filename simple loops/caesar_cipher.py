def caesar_cipher():
    string_input = input()
    for i in range(len(string_input)):
        if string_input[i] == "X":
            char = 65
        elif string_input[i] == "Y":
            char = 66
        elif string_input[i] == "Z":
            char = 67
        else:
            char = ord(string_input[i]) + 3
        print(chr(char), end = "")
        
caesar_cipher()