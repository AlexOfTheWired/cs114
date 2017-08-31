from random import randint
from time import sleep

fortune_list = [
'How would I know',
'Cool',
'Potentially',
'Probably',
'Sure, why not',
'Maybe',
'...',
'Try again later',
'I don\'t know'
]


def prompt_for_name():
    return input("Hello. What is your name...?    ")

def get_fortune():
    r = randint (0, len(fortune_list))
    return fortune_list[r]


def print_fortune_part1(name):
    return name + ", your fortune is... \n"

def print_fortune_part2(fortune):
    return fortune


def main():
    name     = prompt_for_name()
    fortune  = get_fortune()
    message1 = print_fortune_part1(name)
    message2 = print_fortune_part2(fortune)

    print (message1)
    sleep(1)
    print (message2)


if __name__ == '__main__':

    main()
