def square_root():
    num = int(input())
    half = num / 2
    power = 10 ** -12
    while(abs(half*half) - num >power and abs(half*half) - num != power):
        half = (half + num / half) / 2
    print(half)

square_root()