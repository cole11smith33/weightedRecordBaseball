import csv
csv_path = "outputResults/2024results.csv"
file_path = "data/resultsOfEveryRegSeasonGameIn2024.txt"

#function to parse the line
#e.g New York Mets (0) @ Atlanta Braves (3) Boxscore becomes New York Mets (0) @ Atlanta Braves (3)     
def parseLine(parsedLine):
        #remove unneed whitespace
        parsedLine = parsedLine.strip()
        if not parsedLine: # case where line is empty, to clean up data more
             return None
        if "2024" in parsedLine: # remove lines with the date games were played, to clean up the data more
             return None
        parsedLine = parsedLine.replace("Boxscore", "") # removing the filler text on each line of the dataset

        return parseIntoResults(parsedLine)


# temp code, will make more efficient by avoiding the loop and just using the built-in split function
def parseIntoResults(parsedLine):
        datapoint = ""
        mode=0
        teams = parsedLine.split("@") # New York Mets (0) @ Atlanta Braves (3), by spliting at the @ we get the results of the home and away team seperated
        for char in teams[0]:
            if char == "@":
                continue
            if char == "(" and mode==0:
                mode=1 #mean that we have collected our first datapoint 
                awayTeam=datapoint.strip()
                datapoint = ""
                continue
            if char == ")" and mode==1:
                awayScore = datapoint
                awayScore = int(awayScore) 
                datapoint = ""
                mode=0
                continue
            datapoint = datapoint+char
        for char in teams[1]:
            if char == "@":
                 continue
            if char == "(" and mode==0:
                mode=1 #mean that we have collected our first datapoint 
                homeTeam= datapoint.strip()
                datapoint = ""
                continue
            if char == ")" and mode==1:
                homeScore = datapoint
                homeScore = int(homeScore) 
                datapoint = ""
                mode=0
                continue
            datapoint = datapoint+char
        addBoxscoreToCSV(awayTeam, awayScore, homeTeam, homeScore)
        return(awayTeam, awayScore, homeTeam, homeScore)


def addBoxscoreToCSV(awayTeam, awayScore, homeTeam, homeScore):
     with open(csv_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow([awayTeam, awayScore, homeTeam, homeScore])

#read file
try:
    with open(file_path, 'r') as seasonData:
        #read the seasonData file line by line
        for line in seasonData:
            result = parseLine(line)
            if result:
                 print(result)
except FileNotFoundError: # situation where the file is unable to be located
    print("File " + file_path + "could not be located")
except Exception as e: # an error not related to file location has occured
    print("Unable to properly read file")


#testing purposes

#parseIntoResults("New York Mets (0) @ Atlanta Braves (3)")
#addBoxscoreToCSV("New York Mets", "0", "Atlanta Braves", "3")


        