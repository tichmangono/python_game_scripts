import random
# Dice Roll Simulator by 
"""
This program will simulate rolling a dice which has 6 sides
        author: TMangono
        Date: 5/16/15
        Project: personal review, practice

"""

def dice_roll():
    n=0
    print ('Welcome to the Dice Simulator Application')
    myRoll=input("Would you like to roll the dice? (Y/N): ")
    while myRoll not in ('Y', 'y', 'N', 'n'):
        print('Your input is invalid, let us try this one more time.')
        myRoll=input("Would you like to roll the dice? (Y/N): ")
    while myRoll=="Y" or myRoll=="y":
        #roll again
        n=random.randint(1,6)
        print ('You rolled a ' + str(n))
        myRoll=input("Would you like to roll the dice again? (Y/N): ")
    if myRoll=="N" or myRoll=="n":
        print('Game Over, Thank you for playing!')
dice_roll()
