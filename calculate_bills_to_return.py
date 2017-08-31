fifties_value  = 50
twenties_value = 20
tens_value     = 10
fives_value    = 5
singles_value  = 1

def calculate_bills_to_return(change):
    
    # Fifties Variable
    fifties_number = change // fifties_value
    fifties_remainder = change - (fifties_number * fifties_value)

    # Twenties Variable
    twenties_number     = change // twenties_value
    twenties_remainder  = fifties_number - (twenties_number * twenties_value)

    # Tens Variables
    tens_number        = twenties_remainder // tens_value
    tens_remainder     = twenties_remainder - (tens_number * tens_value)

    # Fives Variables
    fives_number      = tens_remainder // fives_value
    fives_remainder   = tens_remainder - (fives_number * fives_value)

    # Singles Variables
    singles_number      = fives_remainder // singles_value
    singles_remainder   = fives_remainder - (singles_number * singles_value)

    coins_to_return     = (quarters_number,    dimes_number,    nickels_number,    pennies_number)
    remainders          = (quarters_remainder, dimes_remainder, nickels_remainder, pennies_remainder)

    return (coins_to_return, remainders)
