def temperature_conversion():
    print("degrees_celcius  degrees_fahrenheit")
    for i in range(11):
        print('{:5}'.format(" "), i*10, end = " ")
        print('{:15}'.format(" "),(i*10 * 9//5) + 32)
temperature_conversion()