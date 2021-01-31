#!/usr/bin/env python3
import sys
import random
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"
number = random.randrange(1,3)
totguess = 3
while(totguess != 0):
    guess = input("Guess a number from 1 to 10. You have "  + str(totguess) + " guesses left: ") 
    guess = int(guess)
    
    if guess == number: 
        print("Great job! You got it!") 
        break
    if  guess != number:
        totguess -= 1
        if guess != number and totguess == 0:
            print("Looks like you've run out of guesses!")
            break
        print("Sorry my guy, try again!")
   
