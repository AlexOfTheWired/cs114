


def calculate_coins_to_return(change):

    change = int(input("Amount Tendered?"))

    quarters_value  = 25
    dimes_value     = 10
    nickels_value   = 5
    pennies_value   = 1

    quarters_number  = change // quarters_value
    dimes_number     = change // dimes_value
    nickels_number   = change // nickels_value
    pennies_number   = change // pennies_value

    q_remainder = change - (quarters_number * quarters_value)
    d_remainder = change - (dimes_number * dimes_value)
    n_remainder = change - (nickels_number * nickels_value)


    if change < 100:
        print (str( quarters_number) + " Quarters")
        print ("Change after quaters : " + str(q_remainder))
        if q_remainder == 24:
            print("PASS")
    if q_remainder < 25:
        print (str( dimes_number) + " Dimes")
        print ("Change after dimes : " + str(d_remainder))
        if q_remainder == 4:
            print("PASS")


calculate_coins_to_return(100)
