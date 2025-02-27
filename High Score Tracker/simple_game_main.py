#This is Nicole's simple game user interface
from simple_games import one_ten as ten, one_hundred as hundred


def simple_game_main():
    while True:
        choice = input("\nWelcome to the SIMPLE GUESSING GAME!\n What would you like to do? \n 1) Guess 1-10\n 2) Guess 1-100\n 3) EXIT to the main menu\n")
        if choice == '1':
            while True:
                oneTen = ten()
                if 'end' in oneTen:
                    break  
        elif choice == '2':
            while True:
                oneHundred = hundred()
                if 'end' in oneHundred:
                    break
        elif choice == '3':
            break
