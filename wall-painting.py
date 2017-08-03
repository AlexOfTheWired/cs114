"""All our friends are re-painting one wall of their rooms. They want us to figure out how much it's going to cost. Assume one gallon of paint covers 400 square feet.

Ask the user for:

Width of the wall
Height of the wall
How much a gallon of paint costs
Figure out then print how much it will cost to paint the wall with one coat.

"""
from time import sleep
print(" Width of wall?")
width  = float(input())
print(" Height of wall?")
height = float(input())
print(" cost per gallon")
cost   = float(input())

area             = width * height
gallon_coverage  = 400
cost_per_gallon  = (area / gallon_coverage) * cost


print("It will " + str(cost_per_gallon) +
" moneys to paint wall with one coat.")

sleep(3)

print("Actuall... How many coats of paint?")
coats = float(input())

cost_with_coats   = cost_per_gallon * coats

print("So. It will cost $" + str(cost_with_coats))
