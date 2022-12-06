def birth_to_astrological():
    month = input()
    month = month.lower()
    date = int(input())
    if (month == "december" and date >= 22) or (month == "january" and date <= 19):
        print("Capricorn")
    elif (month == "january" and date >= 20) or (month == "february" and date <= 18):
        print("Aquarius")
    elif (month == "february" and date >= 19) or (month == "march" and date <= 20):
        print("Pisces")
    elif (month == "march" and date >= 21) or (month == "april" and date <= 19):
        print("Aries")
    elif (month == "april" and date >= 20) or (month == "may" and date <= 20):
        print("Taurus")
    elif(month == "may" and date >= 21) or (month == "june" and date <= 20):
        print("Gemini")
    elif (month == "june" and date >= 21) or (month == "july" and date <= 22):
        print("Cancer")
    elif (month == "july" and date >= 23) or (month == "august" and date <= 22):
        print("Leo")
    elif (month == "august" and date >= 23) or (month == "september" and date <= 22):
        print("Virgo")
    elif(month == "september" and date >= 23) or (month == "october" and date <= 22):
        print("Libra")
    elif (month == "october" and date >= 23) or (month == "november" and date <= 21):
        print("Scorpio")
    else:
        print("Sagittarius")
birth_to_astrological()