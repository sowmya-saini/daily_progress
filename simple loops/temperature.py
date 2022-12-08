def temperature_conversion():
    print("degrees_celcius  degrees_fahrenheit")
    for i in range(11):
        print("   ", i*10, end = "                ")
        print((i*10 * 9//5) + 32)
temperature_conversion()