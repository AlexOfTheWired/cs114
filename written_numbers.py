num = int(input("A number between 1 and 99:  "))

tens = num // 10
ones = num % 10

if tens == 9:
    tens_words = "ninety"
