import random

# Guess The Number Challenge
"""
This challenge will generate random numbers and the player will try to guess
what the number is. The game will either confirm if the guess is correct or tell
player if they guessed above or below the number.

    author:Tich Mangono
    date:5/16/15
    project: practice, independent review

"""
print ('Play Guess the Number!')

def guess_number():
    status='y'
    #get input from player
    n=random.randint(0,500)
    print (n)
    myGuess=input('Enter your best guess for the number between 0 and 500:')
    #check input, data validation
    while int(myGuess) not in range(500):
        print('Your input is invalid')
        myGuess=input('Enter your best guess for the number between 0 and 500:')
    while int(myGuess)==n:
        status='n'
        print('Congratulations! Your guess is as good as mine!') 
        status=input('Play again (Y/N?)')
        if status in ('y', 'Y'):
            n=random.randint(0,500)
            print (n)
            myGuess=input('Enter your best guess for the number between 0 and 500:')
        else:
            print('Goodbye!')
            
    while int(myGuess)!=n:
    
        while int(myGuess)<n and int(myGuess) in range(500):
            print('Your guess is too low! try again')
            myGuess=input('Enter your best guess for the number between 0 and 500:')
            if int(myGuess)==n:
                print('Congratulations! Your guess is as good as mine!') 
                status=input('Play again (Y/N?)')
                if status in ('y', 'Y'):
                    n=random.randint(0,500)
                    print (n)
                    myGuess=input('Enter your best guess for the number between 0 and 500:')
                else:
                    print('Goodbye!')

        while int(myGuess)>n and int(myGuess) in range(500):
            print('Your guess is too high!, try again')
            myGuess=input('Enter your best guess for the number between 0 and 500:')
            if int(myGuess)==n:
                status='n'
                print('Congratulations! Your guess is as good as mine!') 
                status=input('Play again (Y/N?)')
                if status in ('y', 'Y'):
                    n=random.randint(0,500)
                    print (n)
                    myGuess=input('Enter your best guess for the number between 0 and 500:')
                else:
                    print('Goodbye!')

guess_number()
