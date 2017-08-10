def calculate_coins_to_return(change):

    change = int(input("Amount Tendered?"))

    quarters_value   = 25
    dimes_value      = 10
    nickels_value    = 5
    pennies_value    = 1

# Quarters Variables
    quarters_number  = change // quarters_value
    q_remainder      = change - (quarters_number * quarters_value)

# Dimes Variables
    dimes_number     = q_remainder // dimes_value
    d_remainder      = q_remainder - (dimes_number * dimes_value)

# Nickles Variables
    nickels_number   = d_remainder // nickels_value
    n_remainder      = d_remainder - (nickels_number * nickels_value)

# Pennies Variables
    pennies_number   = n_remainder // pennies_value
    p_remainder      = n_remainder - (pennies_number * pennies_value)

    if change < 100:
        print (str( quarters_number) + " Quarters")
        print ("Change after quaters : " + str(q_remainder))
        if q_remainder == 24:
            print("PASS")
        else:
            print("FAIL!!!")

    if q_remainder < 25:
        print (str( dimes_number) + " Dimes")
        print ("Change after dimes : " + str(d_remainder))
        if d_remainder == 4:
            print("PASS")
        else:
            print("FAIL!!!")

    if d_remainder < 10:
        print (str( nickels_number) + " Nickles")
        print ("Change after nickles : " + str(n_remainder))
        if n_remainder == 4:
            print("PASS")
        else:
            print("FAIL!!!")

    if n_remainder < 5:
        print (str( pennies_number) + " Pennies")
        print ("Change after pennies : " + str(p_remainder))
        if p_remainder == 0:
            print("PASS")
        else:
            print("FAIL!!!")

calculate_coins_to_return(100)
