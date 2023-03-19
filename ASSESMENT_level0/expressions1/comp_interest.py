def compound_interest():
    money_deposited = float(input())
    year1 = 4 * money_deposited /100
    year1_amt = year1 + money_deposited
    year2 = 4 * year1_amt/100
    year2_amt = year2 + year1_amt
    year3 = 4 * year2_amt/100
    year3_amt = year3 + year2_amt
    print("After one year the amount is:", format(year1_amt, ".2f"))
    print("After two years the amount is :", format(year2_amt, ".2f"))
    print("After three years the amount is:", format(year3_amt, ".2f"))
compound_interest()