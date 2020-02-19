import csv
import copy

data = open('votes_all.csv', encoding="utf8")
vote_list = csv.reader(data)
finalScores = []

def cleanData(x):
	clean_birds = []
	for row in x:
		length = len(row)
		makeListsEqualLength(row, length)
		clean_birds.append(row)
	return clean_birds

def makeListsEqualLength(row, length):
	x = 0
	req = 6 - length
	while x < req:
		row.append("novote")
		x+=1

def createScoreboard(x):
	scoreDict = {}
	for vote in x:
		isitthere = scoreDict.get(vote[1], False)
		if isitthere == False:
			scoreDict[vote[1]] = 1
		else:
			scoreDict[vote[1]] +=1
	return scoreDict


def youAreTheWeakestLink(x, y):
	global finalScores
	localcopy = copy.deepcopy(x) # create a local copy of the scoreboard dict
	for burd, score in localcopy.items(): #for each bird in the copy
		minvalue = min(x.values()) #find the bird with the lowest score
		if score == minvalue: #check the score to see if it's the lowest scoring bird
			loser = burd #if it is, it's the loser
			finalScores.append([burd, score])# add its final score to the finalscore object
			del x[burd] #deletes the loser from the scoreboard
			contender = nextPlease(y, burd) #identifies the next contender
			levelUp(x, contender) #adds a vote to the second preference			
	return(finalScores)


def nextPlease(votes, loser):
	for vote in votes:
		if vote[1] == loser:
			del vote[0]
			vote.append("novote")
			return vote[1]

def levelUp(x, contender):
	if contender in x:
		x[contender] += 1


def burdIsTheWord(x, y):
	minvalue = min(x.values())
	while len(x) > 0:
		youAreTheWeakestLink(x, y)




cleanVoteList = cleanData(vote_list)
scoreboard = createScoreboard(cleanVoteList)
burdIsTheWord(scoreboard,cleanVoteList)


with open('birdoftheyear.csv', 'w', newline="") as csv_file:
	writer = csv.writer(csv_file)
	for bird in finalScores:
		writer.writerow([bird[0], bird[1]])
