#!/bin/python3

f = open("scores.out", "r")

participants = {}                        # an empty dictionary
for line in f:
    entry = line.strip().split(",")     # strip() & split() chained: split() produces a list of items delimited with ,
    participant = entry[0];
    score = entry[1]
    participants[participant] = score   # populate the dictionary
    print(participant + ": " + score)   # print an entry at a time

f.close()
print(participants)     # print the dictionary as a whole
