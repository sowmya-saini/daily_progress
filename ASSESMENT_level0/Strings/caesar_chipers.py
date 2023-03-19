def encrpytWithCaesar(stringinput, shift_amount):
    for i in stringinput:
        if i >='a' and i <= 'z':
            val = ord(i)
            position = val - ord('a')
            final = (position + shift_amount) % 26 + ord('a')
            print(chr(final), end = "")
        elif i >='A' and i <= 'Z':
            val = ord(i)
            position = val - ord('A')
            final = (position + shift_amount) % 26 + ord('A')
            print(chr(final), end = "")
        else:
            print(i, end = "")
encrpytWithCaesar("ABHINAY@chinna", 3)
        