def prompt_for_number():
    """prompts the user to input number between 0 and 99."""
    return int(input('A number between 0 and 99: '))

def get_tens_number(num):
    """ Takes number and divides by 10, throws out remainder. """
    tens = num // 10

    return tens

def get_ones_number(num):
    """ Takes number and divides by 10, returns remainder. """
    ones = num %  10

    return ones

def tens_number_to_word(tens):
    """ """
    if tens       == 9:
        tens_word = "ninety"
    elif tens     == 8:
        tens_word = "eight"
    elif tens     == 7:
        tens_word = "seventy"
    elif tens     == 6:
        tens_word = "sixty"
    elif tens     == 5:
        tens_word = "fifty"
    elif tens     == 4:
        tens_word = "forty"
    elif tens     == 3:
        tens_word = "thirty"
    elif tens     == 2:
        tens_word = "twenty"
    else:
        tens_word = ""

    return tens_word

def ones_number_to_word(ones):
    """ """
    if ones        == 9:
        ones_word = "nine"
    elif ones      == 8:
        ones_word = "eight"
    elif ones      == 7:
        ones_word = "seven"
    elif ones      == 6:
        ones_word = "six"
    elif ones      == 5:
        ones_word = "five"
    elif ones      == 4:
        ones_word = "four"
    elif ones      == 3:
        ones_word = "three"
    elif ones      == 2:
        ones_word = "two"
    elif ones      == 1:
        ones_word = "one"
    else:
        ones_word = "zero"

    return ones_word

def irregular_numbers_to_words(ones):
    """ """
    if ones == 1:
        output = 'eleven'
    elif ones == 2:
        output = 'twelve'
    elif ones == 3:
        output = 'thirteen'
    else:
        output = ones_word + 'teen'

def regular_numbers_message(tens, ones, tens_word, ones_word):
    if ones == 0:
        return tens_word
    elif tens == 0:
        return ones_word

    return tens_word + "-" + ones_word

def irregular_numbers_message(ones, ones_word):
    if ones == 1:
        output = 'eleven'
    elif ones == 2:
        output = 'twelve'
    elif ones == 3:
        output = 'thirteen'
    else:
        output = ones_word + 'teen'

    return output

def written_numbers_message(tens, ones, tens_word, ones_word):
    if tens    == 1:
        output = irregular_numbers_message(ones, ones_word)
    else:
        output = regular_numbers_message(tens, ones, tens_word, ones_word)

    return output

def main():
    num       = prompt_for_number()
    tens      = get_tens_number(num)
    ones      = get_ones_number(num)
    tens_word = tens_number_to_word(tens)
    ones_word = ones_number_to_word(ones)
    output    = written_numbers_message(tens, ones, tens_word, ones_word)

    print (output)
if __name__ == '__main__':
    main()
