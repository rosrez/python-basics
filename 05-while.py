#!/bin/python3

# a basic while loop
counter = 0
while counter < 5:
    print("Hello " + str(counter))
    counter = counter + 1

# infinite loop is also possible
counter = 0
while True:
    print("Hello " + str(counter))
    counter = counter + 1

    if counter >=5:
        break

