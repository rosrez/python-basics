#!/bin/python3

class Greeter(object):
    def __init__(self, name):       # THE CONSTRUCTOR
        self.name = name            # Assign to a FIELD self.name

    def hello(self):
        print("Hello " + self.name)

    def goodbye(self):
        print("Goodbye " + self.name)

ga = Greeter("Adam")
ga.hello()
ga.goodbye()

ge = Greeter("Eve")
ge.hello()
ge.goodbye()
