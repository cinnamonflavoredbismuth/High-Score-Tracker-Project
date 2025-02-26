#High Score Tracker Cecily, Pedro, Nicole, and Sawyer
from simple_game_main import simple_game_main as simple_game #nicole
#from [name of file] import [function name] as complex game #pedro
#from [name of file] import [function name] as simple10_scores #Sawyer
#from [name of file] import [function name] as simple100_scores #sawyer 
#from [name of file] import [function name] as complex_scores #sawyer
def main(): #Cecily did this
    run=True
    while run==True:
        try:
            choose= int(input("""What do you want to do?
                            1. See a scoreboard
                            2. Play a game
                            3. Leave\n"""))
            if choose==1:#dispay scores
                stay=True
                while stay==True:
                    try:
                        choose_board=int(input("""What do you want to do?
                                            1. 1-10 scoreboard
                                            2. 1-100 scoreboard
                                            3. complex scoreboard
                                            4. exit\n"""))
                        if choose_board==1:
                            print(simple10_scores())
                            break
                        elif choose_board==2:
                            print(simple100_scores())
                            break
                        elif choose_board==3:
                            print(complex_scores())
                            break
                        elif choose_board==4:
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
                                            1. simple game
                                            2. complex game
                                            3. exit\n"""))
                        if choose_board==1:
                            simple_game()
                            break
                        elif choose_board==2:
                            complex_game()
                            break
                        elif choose_board==3:
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
main()