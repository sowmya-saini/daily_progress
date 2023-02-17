def PerfectNumbers(number):
    sum_factors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_factors += i
    if sum_factors == number:
        return True
    else:
        return False
# print(PerfectNumbers(28))

def PrintPerfectnum():
    for i in range(1, 10000):
        if PerfectNumbers(i) == True:
            print(i)
PrintPerfectnum()

