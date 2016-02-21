# Hangman Game

"""
Hangman is a guess-the-word game where the player guesses letters of the word with a limit to the number of guesses. 

    author: Tich Mangono
    date: 5/16/15
    project: review, practice

"""

import random

def hang_man():
    print ("Welcome to the world's finest version of HANGMAN!"
            " You get a total of 10 chances to guess one letter at a time."
           " When you think you can guess the full word, enter it at any time."
           " However, be careful, because you only get one chance to guess the full word!"
           " Tip: when you are running out of chances, you might as well guess the word.")
#create the list of words, can expand on this
    Words=("serene", "trust", "humor", "human", "moat", "stupid", "reward", "secure", "define", 
            "family", "destiny", "derail", "master", "fraud", "robot", "house", "earth", "purple", "buzzer",
            "destroy", "cater", "grace", "despair", "amend", "refuse", "deluge"
           , "combust", "python", "lovely", "escape", "disturb", "spirit", "insane",
           "stable", "coward", "hesitate", "conquer", "divide", "instant", "vision", "dream",
           "mango", "apple", "banana", "peach", "avocado", "settle", "stomach", "ankle"
           "foggy", "bottom")        
#select a random word from list
    theWord=random.choice(Words)
    l=len(theWord)
    #print (theWord) #for debugging
    print ('\n OK,the word has a total of '+str(l)+' letters')
    turn = 0
    chances_left=l
    myGuess=[]
    
    for c in theWord:
        myGuess.append("*")
        
    while chances_left>0:
    #get the player to guess
        myLetter=input('\n Enter your letter guess : ').lower()
    #check validity of input, must be a one-letter string
        while myLetter.isalpha()!=True:
            print('\n Invalid input, please enter alphabet characters')
            myLetter=input('\n Enter your one-letter guess : ').lower()
         #catch the guess for the full word
        while myLetter.isalpha()==True and len(myLetter)>=2:
            if myLetter==theWord:
                print('\n PRISONER PARDONED - Great Job, You are a spelling bee!')
                return
            else:
                print ('\n PRISONER HANGED - Terrible guess. You must be a wasp, then :-(')
                print ('The answer was '+ theWord)
                return
        if myLetter.isalpha()==True and len(myLetter)==1 and myLetter not in theWord:
            print('\n Wrong, try again ')
            i=0
            for i in range(l):
                if theWord[i]==myLetter:
                    myGuess[i]=myLetter
                    i +=1
                else:
                    pass
            turn +=1 
            chances_left=10-turn
            hits = l-myGuess.count("*")
            letters_to_go=l-hits
            print (' '.join(myGuess))
            print (' You have ' +str(chances_left)+ ' chances left')
    #continue
        if myLetter.isalpha()==True and len(myLetter)==1 and myLetter in theWord:

            if myLetter in myGuess:
                print ("\n Boring. Try something new.")
            else:
                i=0
                for i in range(l):
                    if theWord[i]==myLetter:
                        myGuess[i]=myLetter
                        i +=1
                    else:
                        pass
                turn +=1 
                chances_left=10-turn
                hits = l-myGuess.count("*")
                letters_to_go=l-hits
                if letters_to_go==0 or myLetter==theWord:
                    print('\n PRISONER PARDONED - Great Job, You are a spelling bee!')
                    return
                else:
                    print ('\n Correct! You exposed '+ str(hits) +' letters so far, '
                       +str(letters_to_go)+ ' more to go' )
                    print (' '.join(myGuess))
                    print ('\n You have ' +str(chances_left)+ ' chances left')
    else:
        print("\n Sorry, you blew all your chances. Goodbye!")
        print (' The answer was '+ theWord)
        return
hang_man()
