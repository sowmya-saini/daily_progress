def encoding_decoding():
    string_input = input()
    shifts = int(input())
    for i in string_input:
        if i >='a' and i <= 'z':
            val = ord(i)
            # print(val)
            position = val - ord('a')
            # print(position)
            final = (position + shifts) % 26 + ord('a')
            # print(final)
        else:
            val = ord(i)
            position = val - ord('A')
            final = (position + shifts) % 26 + ord('A')
        print(chr(final), end = "")

encoding_decoding()