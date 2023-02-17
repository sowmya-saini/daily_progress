def month_to_days():
    month = input()
    month = month.lower()
    if month == "february":
        print("28 or 29 days")
    elif month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december":
        print("31 days")
    else:
        print("30 days")
month_to_days()
