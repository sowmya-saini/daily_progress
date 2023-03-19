def leapyear():
    year = int(input())
    if (year % 400 == 0 or year % 100) and year % 4 ==0:
        print("It is Leap Year")
    else:
        print("It is not leap year")
leapyear()        