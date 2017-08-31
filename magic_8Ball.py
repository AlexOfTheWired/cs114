from random import randint

var1 = 'How would I know'
var2 = 'Cool'
var3 = 'Potentially'
var4 = 'Probably'
var5 = 'Sure, why not'
var6 = 'Maybe'
var7 = '...'
var8 = 'Try again later'
var9 = 'I don\'t know'

r = randint (1, 10)

if r == 1:
    fortune = var1
elif r == 2:
    fortune = var2
elif r == 3:
    fortune = var3
elif r == 4:
    fortune = var4
elif r == 5:
    fortune = var5
elif r == 6:
    fortune = var6
elif r == 7:
    fortune = var7
elif r == 8:
    fortune = var8
elif r == 9:
    fortune = var9

print (fortune)
