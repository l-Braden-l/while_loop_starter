#Braden Leach
#December 6 2024
#While Loop Starter


import random

#----Number Guess Game----#

name = input('Hello what is your name? ')
number = random.randint(1,100)
print(f'\nHi {name} I\'m thinking of a number between 1 and 100.')
guesses_taken = 0

while guesses_taken < 5:
    guess = input('Enter a guess: ')
    guess = int(guess)
    guesses_taken += 1   
    if guess < number:
        print('\nThat was too low.')
    elif guess > number:
        print('\nThat was too high!')
    else: 
        break
if guess == number: 
    print(f'Winner winner, chicken dinner! Congrats {name} you guessed the correct number!')
else: 
    print(f'you lose, too bad. Better luck next time. The right number was {number}')

#----Managing a list----#
temperatures = []
input = 0
while input != -9999:
    guesst = input('Enter a temperature in Fahrenheit (-9999 to quit): ')
    guesst = int(guesst)
    temperatures += guesst
    
    if guesst
