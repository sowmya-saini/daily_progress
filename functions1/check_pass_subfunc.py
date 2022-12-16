def lowercase(str_in):
    if str_in >='a' and str_in <='z':
        return True
    else:
        return False
def uppercase(str_in):
    if str_in >='A' and str_in <='Z':
        return True
    else:
        return False
def digits(str_in):
    if  str_in =='0' or str_in =='1' or str_in =='2' or str_in =='3' or str_in =='4' or str_in =='5' or str_in =='6' or str_in =='7' or str_in =='8' or str_in <= '9':
        return True
    else:
        return False
def CheckPassword():
    password = input()
    lower = 0
    upper = 0
    digit = 0
    if len(password) >= 8:
        for i in password:
            if lowercase(i) == True:
                lower = 1
            elif uppercase(i) == True:
                upper =1
            elif digits(i) == True:
                digit = 1
            
        if lower == 1 and upper == 1 and digit == 1:
            return True
        else:
            return False
    else:
        return False
        

print(CheckPassword())