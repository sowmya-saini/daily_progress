def primecheck(number):
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
        if count == 3:
            break
       
    if count == 2:
        return True
    else:
        return False

def NextPrime(number1):
    given_num = number1 + 1
    greater_number = 0
    while(greater_number != 1):
        if primecheck(given_num) == True:
            greater_number = 1
            break
        given_num += 1
    if greater_number == 1:
        return given_num


print(NextPrime(7))

