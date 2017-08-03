"""All our friends are re-painting one wall of their rooms. They want us to figure out how much it's going to cost. Assume one gallon of paint covers 400 square feet.

Ask the user for:

Width of the wall
Height of the wall
How much a gallon of paint costs
Figure out then print how much it will cost to paint the wall with one coat.

"""
print(" Width of wall?")
width  = float(input())
print(" Height of wall?")
height = float(input())
print(" cost per gallon")
cost   = float(input())

area             = width * height
gallon_coverage  = 400
overall_cost     = (area / gallon_coverage) * cost

print("It will  " + str(overall_cost)
 + " moneys to paint wall with one coat." )
