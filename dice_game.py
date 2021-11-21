#This is a dice game
#Import the random module in order to access the randit() method
import random
print('Welcome to CH_Africa dice game!')
#Include a loop to keep the game running
while True:
    start = input("Kindly enter 'start' to roll the dice OR 'exit' to quit the game: ")

#include a conditional statement to start or end the program
    if start == 'exit':
        print('\nThank you for playing')
        break

#Instruct randit() method to randomly pick an integer between 1 and 6(including 1 and 6)
    dice_number = random.randint(1, 6)

#Add conditional statements for each number
    if dice_number == 1:
        print('\nDrop the dice!')
    elif dice_number == 2:
        print(f'\nYou rolled {dice_number}')
    elif dice_number == 3:
        print(f'\nRoll Again!')
    elif dice_number == 4:
        print(f'\nYou rolled {dice_number}')
    elif dice_number == 5:
        print(f'\nYou rolled {dice_number}')
    elif dice_number == 6:
        print('\nMove to the next step')