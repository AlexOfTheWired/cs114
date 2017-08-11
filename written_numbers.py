num = int(input("A number between 1 and 99:  "))

tens = num // 10
ones = num % 10

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


if ones        == 9:
    ones_words = "nine"
elif ones      == 8:
    ones_words = "eight"
elif ones      == 7:
    ones_words = "seven"
elif ones      == 6:
    ones_words = "six"
elif ones      == 5:
    ones_words = "five"
elif ones      == 4:
    ones_words = "four"
elif ones      == 3:
    ones_words = "three"
elif ones      == 2:
    ones_word  = "one"
