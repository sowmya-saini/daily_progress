def is_prime(number):
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
        if count == 3:
            break
    if count == 2:
        return "It is a prime number"
    else:
        return "It is not a prime number"
print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(5))
print(is_prime(762))
