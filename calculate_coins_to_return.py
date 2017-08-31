quarters_value   = 25
dimes_value      = 10
nickels_value    = 5
pennies_value    = 1

def prompt_for_amount_tendered():
    return int(input("Amount Tendered?"))

def calculate_coins_to_return(change):

    # Quarters Variables
    quarters_number     = change // quarters_value
    quarters_remainder  = change - (quarters_number * quarters_value)

    # Dimes Variables
    dimes_number        = quarters_remainder // dimes_value
    dimes_remainder     = quarters_remainder - (dimes_number * dimes_value)

    # Nickles Variables
    nickels_number      = dimes_remainder // nickels_value
    nickels_remainder   = dimes_remainder - (nickels_number * nickels_value)

    # Pennies Variables
    pennies_number      = nickels_remainder // pennies_value
    pennies_remainder   = nickels_remainder - (pennies_number * pennies_value)

    coins_to_return     = (quarters_number,    dimes_number,    nickels_number,    pennies_number)
    remainders          = (quarters_remainder, dimes_remainder, nickels_remainder, pennies_remainder)

    return (coins_to_return, remainders)

def get_quarters_number(quarters_number):
    return "Quarters: " + strquarters_number


def test_calculate_coins_to_return(change, coin_numbers, coin_remainders, coin_expectations):

    quarters_number = coin_numbers[0]
    dimes_number    = coin_numbers[1]
    nickels_number  = coin_numbers[2]
    pennies_number  = coin_numbers[3]

    q_remainder = coin_remainders[0]
    n_remainder = coin_remainders[1]
    d_remainder = coin_remainders[2]
    p_remainder = coin_remainders[3]

    # this works...
    #q_expectations = coin_expectations[0]
    #n_expectations = coin_expectations[1]
    #d_expectations = coin_expectations[2]
    #p_expectations = coin_expectations[3]

    # ...or this works, they do the same thing.
    q_expectations, n_expectations, d_expectations, p_expectations = coin_expectations

    if change < 100:
        print (str(quarters_number) + " Quarters")
        print ("Change after quaters : " + str(q_remainder))
        if q_remainder == q_expectations:
            print("PASS")
        else:
            print("FAIL!!!")

        if q_remainder < quarters_value:
            print (str(dimes_number) + " Dimes")
            print ("Change after dimes : " + str(d_remainder))
            if d_remainder == d_expectations:
                print("PASS")
            else:
                print("FAIL!!!")

        if d_remainder < dimes_value:
            print (str(nickels_number) + " Nickles")
            print ("Change after nickles : " + str(n_remainder))
            if n_remainder == n_expectations:
                print("PASS")
            else:
                print("FAIL!!!")

        if n_remainder < nickels_value:
            print (str(pennies_number) + " Pennies")
            print ("Change after pennies : " + str(p_remainder))
            if p_remainder == p_expectations:
                print("PASS")
            else:
                print("FAIL!!!")

def main():



#
#  test 01
#
#print("\nExecuting Test 01.")
#test_01_change = 99
#test_01_expectations = (24, 4, 4, 0)
#coins_to_return, remainders = calculate_coins_to_return(test_01_change)
#print ("coins_to_return = " + str(coins_to_return))
#print ("remainders      = " + str(remainders))
#ret = test_calculate_coins_to_return(test_01_change, coins_to_return, remainders, test_01_expectations)

#
#  test 02
#
#print("\nExecuting Test 02.")
#test_02_change = 99
#test_02_expectations = (24, 4, 4, 0)
#coins_to_return, remainders = calculate_coins_to_return(test_02_change)
#print ("remainders      = " + str(remainders))
#ret = test_calculate_coins_to_return(test_02_change, coins_to_return, remainders, test_02_expectations)
