from random import randint
from time import sleep

fortune_list = ['How would I know', 'Cool', 'Potentially',
                'Probably', 'Sure, why not', 'Maybe', '...',
                'Try again later', 'I don\'t know']

var1 = 'How would I know'
var2 = 'Cool'
var3 = 'Potentially'
var4 = 'Probably'
var5 = 'Sure, why not'
var6 = 'Maybe'
var7 = '...'
var8 = 'Try again later'
var9 = 'I don\'t know'


r = randint (0, 9)

def prompt_for_name():
    return input("Hello. What is your name...?    ")

def get_fortune(r):
    if   r == 0:
        fortune = var[0]
    elif r == 1:
        fortune = var[1]
    elif r == 2:
        fortune = var[2]
    elif r == 3:
        fortune = var[3]
    elif r == 4:
        fortune = var[4]
    elif r == 5:
        fortune = var[5]
    elif r == 6:
        fortune = var[6]
    elif r == 7:
        fortune = var[7]
    elif r == 8:
        fortune = var[8]

    return fortune

def print_fortune_part1(name):
    return name + ", your fortune is... \n"

def print_fortune_part2(fortune):
    return fortune


def main():
    name     = prompt_for_name()
    fortune  = get_fortune(r)
    message1 = print_fortune_part1(name)
    message2 = print_fortune_part2(fortune)

    print (message1)
    sleep(2.5)
    print (message2)


if __name__ == '__main__':

    main()
