'''
Small guessing code with imports
17.12.2020
'''
from time import time
from math import floor
from string import ascii_uppercase as aU, ascii_lowercase as aL, digits as d, punctuation as p
from random import randint

allPossible = aU + aL + d + p
randomInt = randint(0,len(allPossible))
randomChar = allPossible[randomInt]
startTime = time()

print("You will be guessing a character based on all keyboard charactors, including upper / lower case and numbers / punctuation, good luck!")

while(True):
    enterChar = input("Guess the random character: ")
    if enterChar == randomChar:
        break
    else:
        print("Wrong, Try again")

print("You are correct with",randomChar)
totalTime = time() - startTime
print("It took you",floor(totalTime),"seconds to find the random charactor")
