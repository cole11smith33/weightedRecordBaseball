file_path = "data/resultsOfEveryRegSeasonGameIn2024.txt"

#function to parse the line
#e.g New York Mets (0) @ Atlanta Braves (3) Boxscore becomes New York Mets (0) @ Atlanta Braves (3)     
def parseLine(parsedLine):
        parsedLine = line.strip()
        if "2024" in parsedLine: # remove lines with the date games were played, to clean up the data more
             parsedLine = ""
        parsedLine = parsedLine.replace("Boxscore", "")
        return parsedLine


# temp code, will make more efficient by avoiding the loop and just using the built-in split function
def parseIntoResults(parsedLine):
        datapoint = ""
        mode=0
        teams = parsedLine.split("@")
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
        return(awayTeam, awayScore, homeTeam, homeScore)


     

#read file
try:
    with open(file_path, 'r') as seasonData:
        #read the seasonData file line by line
        for line in seasonData:
            parsedLine = parseLine(line.strip())
            print(parsedLine)
except FileNotFoundError: # situation where the file is unable to be located
    print("File " + file_path + "could not be located")
except Exception as e: # an error not related to file location has occured
    print("Unable to properly read file")

parseIntoResults("New York Mets (0) @ Atlanta Braves (3)")



        