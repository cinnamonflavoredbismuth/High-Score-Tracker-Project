#Sawyer Wood, Printer for the high scores

import csv
import fontstyle

#File path needed to be sent when calling the function
#file_path = "high_score_printer/highscores.csv"

#It requires the file path to be sent to it
def high_score_printer(file_path):

    #Clearing Screen
    print("\033[H\033[J")

    highscores = []
    player_number = 0

    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            if len(row) != 2:
                continue
            #Creating the dictionary
            item = {
                "name" : row[0],
                "highscore" : int(row[1])
            }

            #Adding the item
            highscores.append(item)
            #sorting it by score
        sorted_by_score = sorted(highscores, key = lambda gamer: gamer["highscore"], reverse = True)

        #Printing all the scores with the names and ranks
        print("\tRank    Name    Score")
        for x in sorted_by_score:
            player_number += 1
            if player_number <= 5:
                #Printing the 5 top scores with cool special colors!
                if player_number == 1:
                    print(fontstyle.apply(f"\t{player_number}\t{x['name']}\t{x['highscore']}", "underline/bold/Italic/yellow"))
                elif player_number == 2:
                    print(fontstyle.apply(f"\t{player_number}\t{x['name']}\t{x['highscore']}", "bold/Italic/green"))
                elif player_number == 3:
                    print(fontstyle.apply(f"\t{player_number}\t{x['name']}\t{x['highscore']}", "Italic/cyan"))
                elif player_number == 4:
                    print(fontstyle.apply(f"\t{player_number}\t{x['name']}\t{x['highscore']}", "purple"))
                elif player_number == 5:
                    print(fontstyle.apply(f"\t{player_number}\t{x['name']}\t{x['highscore']}", "red"))
            else:
                break
    #Back to where you came from
    return