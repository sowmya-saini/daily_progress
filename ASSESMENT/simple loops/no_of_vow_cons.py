def no_of_vow_cons():
    string_input = input()
    string_input = string_input.lower()
    vowels = 0
    consonants = 0
    for i in range(len(string_input)):
        if string_input[i] == "a" or string_input[i] == "e" or string_input[i] == "i" or string_input[i] == "o"  or string_input[i] == "u":
            vowels += 1
        else:
            consonants += 1
    print("The number of vowels are", vowels)
    print("The number of consonants are", consonants)
no_of_vow_cons()
