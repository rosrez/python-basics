#!/bin/python3

f = open("countries2.txt", "r")

countries = []

for line in f:              # iterate through every line in the file
    line = line.strip()     # strip trailing whitespace
    countries.append(line)

f.close()
print(countries)
print("We have " + str(len(countries)) + " countries")

print("Countries that start with T")
for country in countries:
    if country[0] == "T":
        print(country)

