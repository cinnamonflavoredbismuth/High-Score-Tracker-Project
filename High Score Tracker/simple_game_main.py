#This is Nicole's simple game user interface
from simple_games import one_ten as ten, one_hundred as hundred


def simple_game_main():
    while True:
        choice = input("\nWelcome to the SIMPLE GUESSING GAME!\n What would you like to do? \n 1) Guess 1-10\n 2) Guess 1-100\n 3) EXIT to the main menu\n")
        if choice == '1':
            while True:
                score, oneTen, username = ten()
                if 'end' in oneTen:
                    with open('High Score Tracker/simple_game1-10.csv','a') as file:
                        file.write(f"{username},{score}") 
                    break       
        elif choice == '2':
            while True:
                score, oneHundred, username = hundred()
                if 'end' in oneHundred:
                    with open('High Score Tracker/simple_game1-100.csv','a') as file:
                        file.write(f"{username},{score}")
                    break
        elif choice == '3':
            break
