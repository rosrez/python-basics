#!/bin/python3

f = open("scores.out", "w")

while True:
    participant = input("Participant name> ")
    if participant == "":
        break

    score = input("Score for " + participant + "> ")

    f.write(participant + "," + score + "\n")           # the write() method

f.close()
