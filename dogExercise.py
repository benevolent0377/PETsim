import math, random

day = 1
hour = 1

class Dog:
    
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
        self.name = "None"
        self.tricks = ["Sit", "Jump", "Balance-On-Nose"]
        self.hunger = 5
        self.happiness = 5
        self.sleepiness = 0
        self.anxiety = 0

    def rename(self, name):
        self.name = name

    def teachATrick(self, trick):

        if(self.hasEnergy(-7)):
            self.tricks.append(trick)

            self.changeValues(2, 7)

    def forget(self, trick):

        self.tricks.remove(trick)

    def giveTreat(self):

        self.changeValues(0, -1)
        self.changeValues(2, -1)
        self.changeValues(3, -2)

        timePassed(1)
            
    def feed(self):
        
        self.changeValues(0, -5)
        self.changeValues(2, -2)

        timePassed(1)
    
    def hasEnergy(self, energyDrain):
        if self.sleepiness < 10 + energyDrain:
            return True
        else:
            print("{self.name} is too tired to do that right now...")
            return False

    def isCalm(self, minCalmness):

        if self.anxiety <= minCalmness:
            return True
        else:
            return False

    def sleep(self):
    
        if (self.isCalm(7)):
            self.changeValues(2, -10)
            self.changeValues(0, -2)

            timePassed(2)
    def changeValues(self, var, shift, maximum = 10):
        match var:
            
            # hunger
            case 0:
                self.hunger += shift

                if self.hunger < 0:
                    self.hunger = 0
                elif self.hunger > maximum:
                    self.hunger = maximum
            # happiness
            case 1:
                self.happiness += shift

                if self.happiness < 0:
                    self.happiness = 0
                elif self.happiness > maximum:
                    self.happiness = maximum
            # sleepiness
            case 2:
                self.sleepiness += shift

                if self.sleepiness < 0:
                    self.sleepiness = 0
                elif self.sleepiness > maximum:
                    self.sleepiness = maximum
            # anxiety
            case 3:
                self.anxiety += shift

                if self.anxiety < 0:
                    self.anxiety = 0
                elif self.anxiety > maximum:
                    self.anxiety = maximum
    def readNameTag(self):

        print(f"{self.name} is a {self.breed}, and is {self.color}.")

    def checkUp(self):

        print(f"{self.name} Report:\nHunger: {self.hunger}\nSleepiness: {self.sleepiness}\nHappiness: {self.happiness}\nAnxiety: {self.anxiety}\n\n")


class Owner:

    def __init__(self, name):
        self.name = name
        self.balance = 500
        self.energy = 10
        self.employed = False

    def work(self, job):
        self.

    def sleep(self):

        global day
        global hour

        hour = 1
        day += 1


def timePassed(hours):
    hour += hours

    if hour > 16:
        hour = 16

def hasTime():
    global hour

    if hour > 16:
        return False
    else:
        return True

dog1 = Dog("Terrier", "brown")
dog1.rename("Tommy")
dog2 = Dog("Rotweiler", "spotted-white")
dog2.rename("Laurel")

dog1.checkUp()

dog1.feed()

dog1.teachATrick("Jump")

dog1.checkUp()

dog1.sleep()

dog1.checkUp()
