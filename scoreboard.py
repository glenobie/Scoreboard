import os
import pygame
import pygame.freetype
from layout import HockeyLayout, Layout, LayoutWithClock
from scoreState import GameState
from scoreState import TimedGameState
from numericSurface import NumericSurface

os.environ['SDL_VIDEO_CENTERED'] = '1'

class Colors() :
    CLOCK = (255,255,0,200)  # yellow
    SCORE = (255,0,0,200) # red
    TEXT  = (255,255,255) # white
    PERIOD = (0, 255, 0) # green)

class Fonts:
    NUMERIC_FILE = "LC-bold.otf"
    TEXT_FILE    = "title-sb.ttf"
    TIME_SIZE    = 120
    TEXT_SIZE    = 60
    SCORE_SIZE   = 100
    PENALTY_CLOCK_SIZE = 80


class Scoreboard():

    def __init__(self, window):
       
        self.window = window
        self.layout = HockeyLayout(self.window)

        self.state = GameState()

        self.fontClock = pygame.freetype.Font(Fonts.NUMERIC_FILE, Fonts.TIME_SIZE)
        self.fontScore = pygame.freetype.Font(Fonts.NUMERIC_FILE, Fonts.SCORE_SIZE)
        self.fontPenaltyClock = pygame.freetype.Font(Fonts.NUMERIC_FILE, Fonts.PENALTY_CLOCK_SIZE)
        
        self.minutesText = NumericSurface(self.fontClock, Colors.CLOCK, 0, 2, True)
        self.secondsText = NumericSurface(self.fontClock, Colors.CLOCK, 0, 2, True)
        self.scoreText = NumericSurface(self.fontScore, Colors.SCORE, 0, 2)
        self.penaltyMinutes = NumericSurface(self.fontPenaltyClock, Colors.CLOCK, 0, 1, True)
        self.penaltySeconds = NumericSurface(self.fontPenaltyClock, Colors.CLOCK, 0, 2, True)
        self.period = NumericSurface(self.fontPenaltyClock, Colors.PERIOD, 0, 1, False, 0)

        self.fontText = pygame.freetype.Font(Fonts.TEXT_FILE, Fonts.TEXT_SIZE)

        self.blitList = []
        self.staticBlitList = []

       
    def createStaticBlits(self, blitList) :

        blitList.append( self.layout.getLeftSideCenteredBlit( self.fontText.render("HOME", Colors.TEXT)[0] , Layout.HOME_GUEST_HEIGHT) )
        blitList.append( self.layout.getRightSideCenteredBlit( self.fontText.render("GUEST", Colors.TEXT)[0] , Layout.HOME_GUEST_HEIGHT) )

    def createDynamicBlits(self, blitList) :
        blitList.append( self.layout.getLeftSideCenteredBlit(self.scoreText.getValueAsSurface(self.state.getHomeScore()), Layout.SCORE_HEIGHT)) 
        blitList.append( self.layout.getRightSideCenteredBlit(self.scoreText.getValueAsSurface(self.state.getGuestScore()), Layout.SCORE_HEIGHT)) 

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN :
                # if event.key == pygame.K_ESCAPE:    
                #     self.running = False
                #     break
                    
                if event.key == pygame.K_x:
                     self.state.modifyTime(event.mod & pygame.KMOD_LSHIFT)
                elif event.key == pygame.K_z:
                    self.state.modifyHomeScore(event.mod & pygame.KMOD_LSHIFT)
                elif event.key == pygame.K_c:
                    self.state.modifyGuestScore(event.mod & pygame.KMOD_LSHIFT)
                elif event.key == pygame.K_s: 
                    if event.mod & pygame.KMOD_LSHIFT :                 
                        self.running = False
                else :
                    self.state.processSportSpecificKeys(event)
    
    def update(self):
        self.blitList.clear()
   


    def render(self):
        self.window.fill((0,0,0))
        
        self.window.blits(self.staticBlitList)

        self.createDynamicBlits(self.blitList)
              

        self.window.blits(self.blitList)
        pygame.display.update()    



    def run(self):
        self.running = True 
        while self.running:
            self.processInput()
            self.update()
            self.render()


class TimedScoreboard(Scoreboard) :
    def __init__(self, window):
        Scoreboard.__init__(self, window)    
        # self.state = TimedGameState()
        
   
    def createStaticBlits(self, blitList) :
        Scoreboard.createStaticBlits(self, blitList)
        
        blitList.append( self.layout.getColonBlit( self.fontClock.render(":", Colors.CLOCK)[0]) )
        blitList.append( self.layout.getCentererdBlit(self.fontText.render(self.state.getTimeDivisionName(), Colors.TEXT)[0], LayoutWithClock.PERIOD_HEIGHT) )

    def createDynamicBlits(self, blitList) :
        Scoreboard.createDynamicBlits(self, blitList)
        blitList.append( self.layout.getMinutesBlit(self.minutesText.getValueAsSurface(self.state.getSeconds() // 60))) 
        blitList.append( self.layout.getSecondsBlit(self.secondsText.getValueAsSurface(self.state.getSeconds() % 60))) 
    