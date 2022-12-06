def color_of_square():
    string_input = input()
    number = int(string_input[1])
    alpha = string_input[0]
    if number % 2 == 0:
        if alpha == "a" or alpha == "c" or alpha == "e" or alpha == "g":
            print("WHITE")
        else:
            print("BLACK")
    else:
        if alpha == "a" or alpha == "c" or alpha == "e" or alpha == "g":
            print("BLACK")
        else:
            print("WHITE")
color_of_square()