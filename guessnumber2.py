# Guess The Number Challenge
"""
This challenge will generate random numbers and the player will try to guess
what the number is. The game will either confirm if the guess is correct or tell
player if they guessed above or below the number.

    author:Tich Mangono
    date:5/16/15
    project: practice, independent review

"""

import random
print ('\n Welcome to Guess the Number Challenge. Begin!')

def guess_number():
    status='y'
    #get input from player
    n=random.randint(0,500)
    #print (n) for debugging
    myGuess=input('\n Enter your best guess for the number between 0 and 500:')
    #check input, data validation
    while myGuess.isdigit()==False:
        print('\n Your input is invalid')
        myGuess=input('\n Enter an integer between 0 and 500:')
        
    while int(myGuess) not in range(500):
        print('\n Your input is invalid')
        myGuess=input('\n Enter an integer between 0 and 500:')
    while int(myGuess)==n:
        status='n'
        print('\n Congratulations! Your guess is as good as mine!') 
        status=input('\n Play again (Y/N?)')
        if status in ('y', 'Y'):
            n=random.randint(0,500)
            print (n)
            myGuess=input('\n Enter your best guess for the number between 0 and 500:')
        else:
            print('\n Goodbye!')
            
    while int(myGuess)!=n:
    
        while int(myGuess)<n and int(myGuess) in range(500):
            myGuess=input('\n Too low! try a bigger number: ')
            if int(myGuess)==n:
                print('\n Congratulations! Your guess is as good as mine!') 
                status=input('\n Play again (Y/N?)')
                if status in ('y', 'Y'):
                    n=random.randint(0,500)
                    print (n)
                    myGuess=input('\n Enter your best guess for the number between 0 and 500:')
                else:
                    print('Goodbye!')

        while int(myGuess)>n and int(myGuess) in range(500):

            myGuess=input('\n Too high!, try a smaller number: ')
            if int(myGuess)==n:
                status='n'
                print('\n Congratulations! Your guess is as good as mine!') 
                status=input('\n Play again (Y/N?)')
                if status in ('y', 'Y'):
                    n=random.randint(0,500)
                    print (n)
                    myGuess=input('\n Enter your best guess for the number between 0 and 500:')
                else:
                    print('\n Goodbye!')

guess_number()
