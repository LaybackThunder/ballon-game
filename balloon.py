import pygame
import random
import pygwidgets
from pygame.locals import *
from balloonConstants import *
from abc import ABC, abstractmethod

class Balloon(ABC):
    """This class represents an abstract balloon."""

    popSoundLoad = False
    popSound = None # Load when first balloon is created

    @abstractmethod
    def __init__(self, window, maxWidth, maxHeight, ID,
                oImage, size, nPoints, speedY):
        """Initiate balloon attributes and window reference"""

        self.window = window
        self.ID = ID
        """--------------What is ID???--------------"""
        self.balloonImage = oImage
        self.size = size
        self.nPoints = nPoints
        self.speedY = speedY
        if not Balloon.popSoundLoad: # Load first time only
            Balloon.popSoundLoad = True
            Balloon.popSound = pygame.mixer.Sound('sound\soundsBalloonPop.wav')
        
        balloonRect = self.balloonImage.get_rect() # Get img WxH
        self.width = balloonRect.width
        self.height = balloonRect.height
        # Position ballon within the width of window,
        # but below the button. 
        self.x = random.randrange(maxWidth - self.width)
        self.y = maxHeight + random.randrange(75)
        self.balloonImage.setLoc((self.x, self.y)) 
        """--------------What is setLoc???--------------"""
    
    def clickInside(self, mousePoint):
        """Returns bool and points 
        if balloons was clicked/intersected by mouse coordinates."""

        myRect = pygame.Rect(self.x, self.y, self.width, self.height)
        if myRect.collidepoint(mousePoint):
            Balloon.popSound.play()
            return True, self.nPoints # True here means it was hit
        else:
            return False, 0 # not hit, no points
    
    def update(self):
        """Update balloon vert movement 
        and returns balloon status"""

        self.y -= self.speedY # update y-position by speed
        self.balloonImage.setLoc((self.x, self.y))
        if self.y < -self.height: # off the top of the window
            return BALLOONS_MISSED
        else:
            return BALLOON_MOVING
    
    def draw(self):
        """Draw object to screen."""
        
        self.balloonImage.draw()
        """--------------How is it drawing itself???--------------"""
    
    def __del__(self):
        """Modifying magic method to print message when balloon dies."""

        print(f"{self.size} Balloon {self.ID} is going away.")
    

class BalloonSmall(Balloon):
    """This class represents an small balloon."""

    ballooImage = pygame.image.load('images\lloonSmallRed.png')
    def __init__(self, window, maxWidth, maxHeight, ID):
        oImage = pygwidgets.image(window, (0, 0), 
                                    BalloonSmall.ballooImage)
        super().__init__(window, maxWidth, maxHeight, ID, 
                        oImage, 'Small', nPoints=30, speedY=30)



