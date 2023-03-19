def distance_units():
    feets = float(input("Enter number of feets: "))
    inches = feets * 12
    yards = feets / 3
    miles = feets/5280
    print(feets, "feets is", inches, "inches")
    print(feets, "feets is", yards, "yards")
    print(feets, "feets is", miles, "miles")
distance_units()