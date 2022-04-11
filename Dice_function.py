from random import randint

def roll_dice():
        """Display a random number from one to six"""
        dice_number = randint(1, 6)
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

def enter_game(username):
    "Enter the dice game"
    while True:
        option = input("Enter 'start' to roll the dice OR 'exit' to quit the game: ")
        option = option.lower()
        if option == 'exit':
            exit(f'\nThank you for playing, {username}!')
        elif option == 'start':
            roll_dice()

print('Welcome to CH_Africa dice game!')
username = input("Enter Username: ")
enter_game(username)
#just some changes in files.