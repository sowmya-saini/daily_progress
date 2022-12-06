def vowel_or_consonant():
    character = input()
    if character == 'a' or character == "e" or character == "i" or character == "o" or character == "u":
        print("The entered letter is vowel")
    elif character == "y":
        print("Sometimes y is a constant and sometimes y is a vowel")
    else:
        print("The entered letter is consonant")
vowel_or_consonant()