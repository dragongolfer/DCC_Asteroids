# Michael Kohlmann
# devCodeCamp - Team Helium
# Asteroids Clone
# 6/15/2015

# Helper functions for reading and writing the high score to file.

def readHighScoresFromFile():
    File_name = "high_scores.txt"
    scoreFile = open("high_scores.txt", "r+")
    FileEntries = [line.strip("\n") for line in scoreFile.readlines()]
    scoreList = []
    for each in FileEntries:
        scoreList.append(each.split())
    #print scoreList
    
    return scoreList
    #return [["Mike",200],["Ace",40],["Bob",35],["Charlie",10],["Zero",1]]
    
def insertHighScore(scoreList, name, score):
    scoreToInsert = score
    insertLocation = 0
    insertFound = False
    for each in scoreList:
        if scoreToInsert > int(each[1]):
            insertFound = True
            break
        insertLocation += 1

    if insertFound:
        scoreList.insert(insertLocation,[name,score])
    else:
        scoreList.append([name,score])
        
    while len(scoreList) > 5:
        scoreList.pop(-1)
    return

def saveHighScoresToFile(scoreList):
    File_name = "high_scores.txt"
    File = open(File_name, "w+")
    for each in scoreList:
        File.write("{0} {1}\n".format(each[0],each[1]))
    return
    
    
    
if __name__ == "__main__":
    #Test Area
    scoreList = readHighScoresFromFile()
    insertHighScore(scoreList, "Inserted", 50)
    print scoreList
    saveHighScoresToFile(scoreList)