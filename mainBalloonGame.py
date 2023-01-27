# Balloon main game code

# 1 - Import packages
from pygame.locals import *
import pygame, pygwidgets, sys
from gameMgr import *

# 2 - Defined constants
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
PANEL_HEIGHT = 60
USABLE_WINDOW_HEIGHT = WINDOW_HEIGHT - PANEL_HEIGHT
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds, etc.
oScoreDisplay = pygwidgets.DisplayText(window, (10, USABLE_WINDOW_HEIGHT + 25),
                    'Score: 0', textColor=BLACK, 
                    backgroundColor=None, width=140, fontSize=24)
oStatusDisplay = pygwidgets.DisplayText(window, (180, USABLE_WINDOW_HEIGHT + 25),
                    '', textColor=BLACK, backgroundColor=None,
                    width=300, fontSize=24)
oStartButton = pygwidgets.TextButton(window,
                    (WINDOW_WIDTH - 110, USABLE_WINDOW_HEIGHT + 10), 
                    'Start')

# 5 - Initialize variable
oBalloonMgr = BalloonMgr(window, WINDOW_WIDTH, USABLE_WINDOW_HEIGHT)
playing = False # Wait till user clicks start

# 6 - Loop forever
while True:
    # 7 - Check for handle events
    nPointsEarned = 0
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if playing:
            oBalloonMgr.handleEvents(event)
            theScore = oBalloonMgr.getScore()
            oScoreDisplay.setValue(f'Score: {theScore}')
        elif oStartButton.handleEvent(event):
            oBalloonMgr.start()
            oScoreDisplay.setValue(f'Score: 0')
            playing = True
            oStartButton.disable()
    
    # 8 - Do any "per frame" action
    if playing:
        oBalloonMgr.update()
        nPopped = oBalloonMgr.getCountPopped()
        nMissing = oBalloonMgr.getCountMissied()
        oStatusDisplay.setValue('Popped: ' + str(nPopped) +
                        '   Missing: ' + str(nMissing) +
                        '   Out of: ' + str(N_BALLOONS))
        
        if (nPopped + nMissing) == N_BALLOONS:
            playing = False
            oStartButton.enable()
    
    # 9 - Clear the window
    window.fill(BACKGROUND_COLOR)

    # 10 - Draw all window elements
    if playing:
        oBalloonMgr.draw()
    
    pygame.draw.rect(window, GRAY, pygame.Rect(0,
                USABLE_WINDOW_HEIGHT, WINDOW_WIDTH, PANEL_HEIGHT))
    oScoreDisplay.draw()
    oStatusDisplay.draw()
    oStartButton.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down
    clock.tick(FRAMES_PER_SECOND)
