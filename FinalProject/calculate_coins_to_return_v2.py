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

    return (coins_to_return)

def format_coins_to_return():
    
    return

def main():
    change = prompt_for_amount_tendered()
    coins_to_return = calculate_coins_to_return(change)

    print (coins_to_return)

if __name__ == '__main__':
    main()
