def CheckPassword():
    password = input()
    length_password = len(password)
    number = "no number"
    uppercase = "no uppercase"
    lowercase = "no lowercase"
    if length_password >= 8:
        for i in password:
            if i.isdigit():
                number = "number found"
            elif i.islower():
                lowercase = "lowercase found"
            elif i.isupper():
                uppercase = "uppercase found"
    else:
        return False 
    if number == "number found" and uppercase == "uppercase found" and lowercase == "lowercase found":
        return True
    else:
        return False
print(CheckPassword())