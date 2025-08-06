file_path = "data/resultsOfEveryRegSeasonGameIn2024.txt"

#function to parse the line
#e.g New York Mets (0) @ Atlanta Braves (3)  Boxscore becomes New York Mets (0) @ Atlanta Braves (3)     
def parseLine(parsedLine):
        parsedLine = line.strip()
        parsedLine = parsedLine.replace("Boxscore", "")
        return parsedLine

try:
    with open(file_path, 'r') as seasonData:
        #read the seasonData file line by line
        for line in seasonData:
            parsedLine = parseLine(line.strip())
            print(parsedLine)
except FileNotFoundError: # situation where the file is unable to be located
    print("File " + file_path + "could not be located")
except Exception as e: # another 
    print("Unable to properly read file")



        