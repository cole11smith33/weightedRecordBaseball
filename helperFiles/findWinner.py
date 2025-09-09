import helperFiles.leagueBreakdown as leagueBreakdown
import csv
import pandas as pd

csv_file = "outputResults/2024_results.csv"

def home_or_away_win(row):
        away_team = row[0]
        away_score = row[1]
        home_team = row[2]
        home_score = row[3]
        if away_score > home_score: # away team wins
            return away_team, away_score, home_team, home_score
        elif away_score < home_score: # home team wins
               return home_team, home_score, away_team, away_score  
        else: # case where the game ends in a tie, e.g. the 2016 contest between the pirates and cubs ending in the 6th due to weather with a final score of 1 - 1
            return None, None, None, None # not sure how this will work, come back to fix later     

with open(csv_file, 'r') as season_data_csv:
            reader = csv.reader(season_data_csv, delimiter=",")
            #read the seasonData file line by line
            for row in reader:
                winner, w_score, loser, l_score = home_or_away_win(row)
                print(row[0] + " vs. " + row[2] + " Winner: "  + winner + "(" +  w_score + ")" + " Loser: "  + loser + "(" +  l_score + ")")

