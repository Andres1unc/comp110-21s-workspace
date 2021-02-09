"""Program that outputs one of at least four random, good fortunes."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
fortune_luck: int = randint(1, 9)

print("Your fortune cookie says...")
if fortune_luck < 3:
    print("You're amazing person who will recieve good news this week.")
else: 
    if fortune_luck < 5: 
        print("Everyone loves you and is rooting for your success.")
    else: 
            if fortune_luck < 7:
                print("You will achieve your dreams just keep figthing")
            else:
                print("Your story has just begun good things will come.")
print("Now, go spread positive vibes!")
