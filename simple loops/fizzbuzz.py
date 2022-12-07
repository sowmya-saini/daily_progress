def fizzbuzz():
    number = 100
    for i in range(1, number+1):
        if i % 3 == 0 and i %5 == 0:
            print("fizzbuzz")
        elif i % 5 ==0:
            print("buzz")
        elif i % 3 == 0:
            print("fizz")
        else:
            print(i)
fizzbuzz()