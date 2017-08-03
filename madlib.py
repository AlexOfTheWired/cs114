""" Make a simple madlib filling program. Use the madlib:

The NOUN jumped over the ADJ NOUN.
Prompt the user to input those three placeholder words, save them in variables,
interpolate them into the madlib, then print the final madlib.
"""
print ("The NOUN jumped over the ADJ Noun.")
print ("Type a Noun.")
noun1 = input()
print ("Type an Adjective.")
adj   = input()
print ("Type another Noun.")
noun2 = input()

print ("The " + noun1 + "jumped over the " + adj + " " + noun2 + ".") 
