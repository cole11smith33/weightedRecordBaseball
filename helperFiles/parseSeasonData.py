import csv
csv_path = ["outputResults/2024_results.csv", "outputResults/2023_results.csv", "outputResults/2022_results.csv", "outputResults/2021_results.csv",
            "outputResults/2020_results.csv", "outputResults/2019_results.csv", "outputResults/2018_results.csv", "outputResults/2017_results.csv",
            "outputResults/2016_results.csv", "outputResults/2015_results.csv", "outputResults/2014_results.csv", "outputResults/2013_results.csv"]
file_path = ["data/2024_reg_season_results.txt", "data/2023_reg_season_results.txt", "data/2022_reg_season_results.txt", "data/2021_reg_season_results.txt",
             "data/2020_reg_season_results.txt", "data/2019_reg_season_results.txt", "data/2018_reg_season_results.txt", "data/2017_reg_season_results.txt",
             "data/2016_reg_season_results.txt", "data/2015_reg_season_results.txt", "data/2014_reg_season_results.txt", "data/2013_reg_season_results.txt"]

#function to parse the line
#e.g New York Mets (0) @ Atlanta Braves (3) Boxscore becomes New York Mets (0) @ Atlanta Braves (3)     
def parseLine(parsedLine):
        #remove unneed whitespace
        parsedLine = parsedLine.strip()
        if "»" in parsedLine:
             return None
        if not parsedLine: # case where line is empty, to clean up data more
             return None
        if str(2024 - i) in parsedLine: # remove lines with the date games were played, to clean up the data more
             return None
        parsedLine = parsedLine.replace("Boxscore", "") # removing the filler text on each line of the dataset
        return parseIntoResults(parsedLine)

# temp code, will make more efficient by avoiding the loop and just using the built-in split function
def parseIntoResults(parsedLine):

        teams = parsedLine.split("@") # New York Mets (0) @ Atlanta Braves (3), by spliting at the @ we get the results of the home and away team seperated

        away_boxscore = teams[0].split("(")
        home_boxscore = teams[1].split("(")

        away_team = away_boxscore[0].strip()
        home_team = home_boxscore[0].strip()

        away_score = away_boxscore[1].replace(")", '').strip() #get rid of the extra ')' char and strip all whitespace
        home_score = home_boxscore[1].replace(")", '').strip()

        addBoxscoreToCSV(away_team, away_score, home_team, home_score)


def addBoxscoreToCSV(awayTeam, awayScore, homeTeam, homeScore):
    writer.writerow([awayTeam, awayScore, homeTeam, homeScore])

#read file
for i in range(len(file_path)):
    try:
        with open(file_path[i], 'r') as seasonData, open(csv_path[i], "w", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            #read the seasonData file line by line
            for line in seasonData:
                result = parseLine(line)
    except FileNotFoundError: # situation where the file is unable to be located
        print("File " + file_path + "could not be located")
    except Exception as e: # an error not related to file location has occured
        print("Unable to properly read file")
        