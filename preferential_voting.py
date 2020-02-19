import csv
import copy

data = open('votes_all.csv', encoding="utf8")
vote_list = csv.reader(data)
birdList = []


# some votes pobjects are missing values - add 

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

cleanVoteList = cleanData(vote_list)