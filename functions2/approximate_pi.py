def approximatepi():
    no_of_approximations = int(input())
    val_approximate = 0
    if no_of_approximations == 1:
        val_approximate = 3
        return val_approximate
    else:
        for i in range(no_of_approximations+1):
            if  i == 0:
                val_approximate = 3
            elif i % 2 != 0:
                val_approximate += 4/((2*i) * (2*i + 1) * (2*i+2))
            else:
                val_approximate -= 4/((2*i) * (2*i + 1) * (2*i+2))
        return val_approximate
print(approximatepi())