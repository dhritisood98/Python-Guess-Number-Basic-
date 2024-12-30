import random
from random import *
print("Hello. What is your name ?")
name = input()
print("Well, " + name + "!" + " I am thinking of a number between 1 to 25 and you have to take a guess in 5 chances.")
number = randint(1, 25)

for guessTaken in range(1,6):
    print("Let's start the game. Take a guess!")
    guessnum = input()

    if int(guessnum) < number:
        print("The guess is too low.")
    elif int(guessnum) > number:
        print("The guess is too high.")
    else:
        break

if int(guessnum) == number:
    print("Well done " + name + "! You guessed my number in " + str(guessTaken) + " guesses.")
else:
    print("You are out of your guesses. The number I was thinking of was " + str(number) + ".Better Luck next time!")
    
    
