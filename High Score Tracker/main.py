#High Score Tracker Cecily, Pedro, Nicole, and Sawyer
from simple_game_main import simple_game_main as simple_game #nicole
from highscore_printer import high_score_printer as score_printer #Sawyer
#from [name of file] import [function name] as [new function name]

def main(): #Cecily did this
    run=True
    while run==True:
        try:
            choose= int(input("""What do you want to do?
1) See a scoreboard
2) Play a game
3) Leave\n"""))
            if choose==1:#dispay scores
                stay=True
                while stay==True:
                    try:
                        choose_board=int(input("""What do you want to do?
1) 1-10 scoreboard
2) 1-100 scoreboard
3) exit\n"""))
                        if choose_board==1:
                            score_printer("High Score Tracker/simple_game1-10.csv")
                            break
                        elif choose_board==2:
                            score_printer("High Score Tracker/simple_game1-100.csv")
                            break
                        elif choose_board==3:
                            break
                        else:
                            print('invalid option')
                    except:
                        print('invalid option')
            elif choose==2:#play game
                stay=True
                while stay==True:
                    try:
                        choose_board=int(input("""What do you want to play?
1) simple game
2) exit\n"""))
                        if choose_board==1:
                            simple_game()
                            break
                        elif choose_board==2:
                            break
                        else:
                            print('invalid option')
                    except:
                        print('invalid option')
            elif choose==3:
                break
            else:
                print('invalid option')
        except:
            print('invalid option')
    return

#Clearing Screen
print("\033[H\033[J")

main()