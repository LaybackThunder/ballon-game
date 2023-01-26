import pygame, random, pygwidgets
from pygame.locals import *
from balloonConstants import *
from balloon import *

#  BalloonMgr manages a list of Balloon objects
class BalloonMgr():
    def __init__(self, window, maxWidth, maxHeight):
        self.window = window
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
    
    def start(self):
        """When called, it resets stats and emptys balloon list.
            Adds new balloon objs with random sizes into list.
        """
        # Object list
        self.ballonList = []
        # Statistics
        self.nPopped = 0
        self.nMissed = 0
        self.score = 0

        # Generate x amount of random balloon object of diferent sizes.
        for balloonNum in range(0, N_BALLOONS):
            randomBalloonClass = random.choice(
                (BalloonSmall, BalloonMedium, BalloonLarge)
                )
            oBalloon = randomBalloonClass(self.window, self.maxWidth, self.maxHeight, balloonNum)
            self.ballonList.append(oBalloon)
    
    def handleEvents(self, event):
        """Checks to see if balloon got hit."""
        if event.type == MOUSEBUTTONDOWN:
            # Go 'reversed' so top-most balloon gets popped
            for oBalloon in reversed(self.ballonList):
                wasHit, nPoints = oBalloon.clickedInside(event.pos)
                if wasHit:
                    if nPoints > 0: #Remove this balloon
                        self.ballonList.remove(oBalloon)
                        self.nPopped += 1
                        self.score += nPoints
                    return # no need to check the other balllons
    
    def update(self):
        """Identifies if balloon went off screen 
            after passing coordinate 0 on the y-axis
        """
        for oBalloon in self.ballonList:
            status = oBalloon.update()
            if status == BALLOONS_MISSED:
                # Balloon went off the top, remove it
                self.ballonList.remove(oBalloon)
                self.nMissed += 1

    def getScore(self):
        return self.score
    
    def getCountPopped(self):
        return self.nPopped
    
    def getCountMissied(self):
        return self.nMissed
    
    def draw(self):
        """Draw all ballon objects in to the screen."""
        for oBalloon in self.ballonList:
            oBalloon.draw()
