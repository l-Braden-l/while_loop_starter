#Braden Leach
#December 6 2024
#While Loop Starter


import random

#----Number Guess Game----#

# name = input('Hello what is your name? ')
# number = random.randint(1,100)
# print(f'\nHi {name} I\'m thinking of a number between 1 and 100.')
# guesses_taken = 0

# while guesses_taken < 5:
#     guess = input('Enter a guess: ')
#     guess = int(guess)
#     guesses_taken += 1   
#     if guess < number:
#         print('\nThat was too low.')
#     elif guess > number:
#         print('\nThat was too high!')
#     else: 
#         break
# if guess == number: 
#     print(f'Winner winner, chicken dinner! Congrats {name} you guessed the correct number!')
# else: 
#     print(f'you lose, too bad. Better luck next time. The right number was {number}')

#----Managing a list----#
temperatures = []
number = 0

while number != -9999:
    number = int(input('Enter a temperature in Fahrenheit (-9999 to quit): '))
    temperatures.append(number)
    
list_length = len(temperatures)

   

if list_length > 0:

    temperatures.pop()
    print(f'Temeratures entered: {temperatures}')
    average = sum(temperatures) / len(temperatures)
    print(f'average temperature:{average:.2f}°F')

# elif list_length < 0: 
#   average = sum(0) / len(0)
