def Tax_tip():
    meal_cost = float(input("Enter the cost of the meal: "))
    tax = 18 *meal_cost /100
    tip = 5 *meal_cost/100
    grand_total = meal_cost + tax + tip
    print("The tax is:", round(tax, 2))
    print("The tip is:", round(tip, 2))
    print("The grand total amount is:", format(grand_total, ".2f"))
Tax_tip()