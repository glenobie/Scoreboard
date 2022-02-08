
import pygame
import pygame.freetype
from layout import Layout, LayoutWithClock
from scoreState import GameState
from numericSurface import NumericSurface

class Colors() :
    CLOCK = (255,255,0,200)  # yellow
    SCORE = (255,0,0,200) # red
    TEXT  = (255,255,255) # white
    PERIOD = (0, 255, 0) # green)

class Fonts:
    NUMERIC_FILE = "LC-bold.otf"
    TEXT_FILE    = "title-sb.ttf"
    TIME_SIZE    = 120
    TEXT_SIZE    = 64
    SCORE_SIZE   = 100
    SMALL_CLOCK_SIZE = 80
    SMALL_TEXT_SIZE = 50

#######################
class Scoreboard():

    def __init__(self, window):
       
        self.window = window
        self.layout = Layout(self.window)

        self.state = GameState()

        
        self.fontScore = pygame.freetype.Font(Fonts.NUMERIC_FILE, Fonts.SCORE_SIZE)
        self.scoreText = NumericSurface(self.fontScore, Colors.SCORE, 2)
        self.fontText = pygame.freetype.Font(Fonts.TEXT_FILE, Fonts.TEXT_SIZE)
        self.fontSmallText = pygame.freetype.Font(Fonts.TEXT_FILE, Fonts.SMALL_TEXT_SIZE)

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
                self.processKeyPress(event)

    def processKeyPress(self, event) :            
        if event.key == pygame.K_x:
            self.state.modifyTime(event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_z:
            self.state.modifyHomeScore(event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_c:
            self.state.modifyGuestScore(event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_s: 
            if event.mod & pygame.KMOD_LSHIFT :                 
                self.running = False
               
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

###################
class TimedScoreboard(Scoreboard) :
    def __init__(self, window):
        Scoreboard.__init__(self, window)   
        self.fontSmallNumber = pygame.freetype.Font(Fonts.NUMERIC_FILE, Fonts.SMALL_CLOCK_SIZE)
        self.fontClock = pygame.freetype.Font(Fonts.NUMERIC_FILE, Fonts.TIME_SIZE)
        self.layout = LayoutWithClock(self.window) 
        self.minutesText = NumericSurface(self.fontClock, Colors.CLOCK, 99)
        self.secondsText = NumericSurface(self.fontClock, Colors.CLOCK, 99, True)     
        self.period = NumericSurface(self.fontSmallNumber, Colors.PERIOD, 9, False)

   
    def processKeyPress(self, event) :            
        Scoreboard.processKeyPress(self, event)
        if event.key == pygame.K_s and not(event.mod & pygame.KMOD_LSHIFT): 
            self.state.modifyPeriod()


    def createStaticBlits(self, blitList) :
        Scoreboard.createStaticBlits(self, blitList)
        
        blitList.append( self.layout.getColonBlit( self.fontClock.render(":", Colors.CLOCK)[0]) )
        blitList.append( self.layout.getCenteredBlit(self.fontText.render(self.state.getTimeDivisionName(), Colors.TEXT)[0], LayoutWithClock.PERIOD_HEIGHT) )

    def createDynamicBlits(self, blitList) :
        Scoreboard.createDynamicBlits(self, blitList)
        blitList.append( self.layout.getMinutesBlit(self.minutesText.getValueAsSurface(self.state.getSeconds() // 60))) 
        blitList.append( self.layout.getSecondsBlit(self.secondsText.getValueAsSurface(self.state.getSeconds() % 60))) 
        blitList.append( self.layout.getCenteredBlit(self.period.getValueAsSurface(self.state.getPeriod() ), LayoutWithClock.PERIOD_VALUE_HEIGHT ) )