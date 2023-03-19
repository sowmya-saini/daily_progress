def bottle_deposits():
    onel_or_less_container = int(input())
    more_than_onel_container = int(input())
    refund = onel_or_less_container*0.10 + more_than_onel_container*0.25
    print("$", format(refund, ".2f"))
bottle_deposits()