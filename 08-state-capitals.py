#!/bin/python

capitals_dict = {
'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
'Hawaii': 'Honolulu',
'Idaho': 'Boise',
'Illinois': 'Springfield',
'Indiana': 'Indianapolis',
'Iowa': 'Des Moines',
'Kansas': 'Topeka',
'Kentucky': 'Frankfort',
'Louisiana': 'Baton Rouge',
'Maine': 'Augusta',
'Maryland': 'Annapolis',
'Massachussetts': 'Boston',
'Michigan': 'Lansing',
'Minnesota': 'Saint Paul',
'Mississipi': 'Jackson',
'Missouri': 'Jefferson City',
'Rhode Island': 'Providence',
'South Carolina': 'Columbia',
'South Dakota': 'Pierre',
'Tennessee': 'Nashville',
'Texas': 'Austin',
'Utah': 'Salt Lake City',
'Vermont': 'Montpelier',
'Virginia': 'Richmond',
'Washington': 'Olympia',
'West Virginia': 'Charleston',
'Wisconsin': 'Madison',
'Wyoming': 'Cheyenne'
}

import random

states = list(capitals_dict.keys())
for i in [1, 2, 3, 4, 5]:
    state = random.choice(states)
    capital = capitals_dict[state]
    capital_guess = input("What is the capital of " + state + "? ")

    if capital_guess == capital:
        print("Correct! Nice job.")
    else:
        print("Incorrect. The capital of " + state + " is " + capital + ".")

print("All done")
