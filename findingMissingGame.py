# I built this file to read the data and find where the missing game was as I had 2429 games in the 2024 regular season instead of the usual 2430 games
# As I found out, this is because in 2024, a game between the Astros and Guardians was cancelled due to a rain delay, and due to its proximity to the end of the season it was never rescheduled
import csv
csv_file = "outputResults/2024results.csv"

team_wins = {

}

def add_to_dict(team):
    if team not in team_wins:
        team_wins[team] = 1
    else:
        team_wins[team] += 1


with open(csv_file, 'r', newline="") as file:
    reader = csv.reader(file)
    season = list(reader)
    season_length = len(season)
    for i in range(season_length):
        add_to_dict(season[i][0])
        add_to_dict(season[i][2])
print(team_wins)
