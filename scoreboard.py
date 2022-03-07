
import pygame
import pygame.freetype
from layout import Layout, LayoutWithClock
from scoreState import GameState
from numericSurface import NumericSurface
from fonts import Fonts
from colors import Colors

#######################
class Scoreboard():

    OUTLINE_SPACING = 8
    OUTLINE_WIDTH   = 2
    SHADOW_WIDTH    = 4

    def __init__(self, window, leftTitle="GUEST", rightTitle="HOME"):
        self.window = window
        self.layout = Layout(self.window)

        self.state = GameState()
        
        self.fontScore = pygame.freetype.Font(Fonts.NUMERIC_FILE, Fonts.SCORE_SIZE)
        self.fontText = pygame.freetype.Font(Fonts.TEXT_FILE, Fonts.TEXT_SIZE)
        self.fontSmallText = pygame.freetype.Font(Fonts.TEXT_FILE, Fonts.SMALL_TEXT_SIZE)
        self.fontSmallNumber = pygame.freetype.Font(Fonts.NUMERIC_FILE, Fonts.SMALLER_NUMBER_SIZE)       
        self.fontVerySmallNumber = pygame.freetype.Font(Fonts.NUMERIC_FILE, Fonts.SMALLEST_NUMBER_SIZE)

        self.scoreText = NumericSurface(self.fontScore, Colors.SCORE, 2)
        self.leftTitle = leftTitle
        self.rightTitle = rightTitle
        self.blitList = []
        self.staticBlitList = []

    def createStaticBlits(self, blitList) :
        blitList.append( self.layout.getLeftSideCenteredBlit( self.fontText.render(self.leftTitle, Colors.TEXT)[0] , Layout.HOME_GUEST_HEIGHT) )
        blitList.append( self.layout.getRightSideCenteredBlit( self.fontText.render(self.rightTitle, Colors.TEXT)[0] , Layout.HOME_GUEST_HEIGHT) )

    def createDynamicBlits(self, blitList) :
        blitList.append( self.layout.getLeftSideCenteredBlit(self.insetSurface(self.scoreText.getValueAsSurface(self.state.getHomeScore())), Layout.SCORE_HEIGHT)) 
        blitList.append( self.layout.getRightSideCenteredBlit(self.insetSurface(self.scoreText.getValueAsSurface(self.state.getGuestScore())), Layout.SCORE_HEIGHT)) 

    def getCombinedSurface(self, firstSurface, secondSurface, spacing) :
        width = firstSurface.get_size()[0] + secondSurface.get_size()[0] + spacing
        if  firstSurface.get_size()[1] > secondSurface.get_size()[1] :
            height = firstSurface.get_size()[1]
            offset = (firstSurface.get_size()[1] - secondSurface.get_size()[1]) / 2
            combinedSurface = pygame.Surface( (width, height ))
            combinedSurface.fill(Colors.BACKGROUND)
            combinedSurface.blit(firstSurface, (0,0))
            combinedSurface.blit(secondSurface, (width - secondSurface.get_size()[0], offset))
        else :
            height = secondSurface.get_size()[1] 
            offset = (secondSurface.get_size()[1] - firstSurface.get_size()[1]) / 2
            combinedSurface = pygame.Surface( (width, height ))
            combinedSurface.fill(Colors.BACKGROUND)
            combinedSurface.blit(firstSurface, (0,offset))
            combinedSurface.blit(secondSurface, (width - secondSurface.get_size()[0], 0))

        return combinedSurface

    def insetSurface(self, surface) :
        w = surface.get_size()[0]
        h = surface.get_size()[1]
        pygame.draw.rect(surface, Colors.OUTLINE, (0, 0, w, h), Scoreboard.OUTLINE_WIDTH)   
        shadowOffset =  NumericSurface.OUTLINE_WIDTH + Scoreboard.SHADOW_WIDTH // 2
        pygame.draw.line(surface, Colors.SHADOW, (shadowOffset, shadowOffset), (w - shadowOffset, shadowOffset), Scoreboard.SHADOW_WIDTH) 
        pygame.draw.line(surface, Colors.SHADOW, (shadowOffset, shadowOffset), (shadowOffset, h-shadowOffset), Scoreboard.SHADOW_WIDTH) 
        pygame.draw.line(surface, Colors.INSET_HIGHLIGHT, (4,h-4), (w-4, h-4), 2) 
        pygame.draw.line(surface, Colors.INSET_HIGHLIGHT, (w-4, 4), (w-4, h-4), 3) 
        
        return surface

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
        self.blitList = []
  
    def render(self):
        self.window.fill(Colors.BACKGROUND)
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
    def __init__(self, window, leftTitle = "GUEST", rightTitle = "HOME"):
        Scoreboard.__init__(self, window, leftTitle, rightTitle)   
        self.fontClock = pygame.freetype.Font(Fonts.NUMERIC_FILE, Fonts.GAME_CLOCK_SIZE)
        self.layout = LayoutWithClock(self.window) 
        self.minutesText = NumericSurface(self.fontClock, Colors.CLOCK, 20)
        self.secondsText = NumericSurface(self.fontClock, Colors.CLOCK, 99, True)     
        self.period = NumericSurface(self.fontSmallNumber, Colors.PERIOD, 9, False)
   
    def processKeyPress(self, event) :            
        Scoreboard.processKeyPress(self, event)
        if event.key == pygame.K_s and not(event.mod & pygame.KMOD_LSHIFT): 
            self.state.modifyPeriod()


    def createStaticBlits(self, blitList) :
        Scoreboard.createStaticBlits(self, blitList)
        
        blitList.append( self.layout.getColonBlit( (self.fontClock.render(":", Colors.CLOCK)[0])) )
        blitList.append( self.layout.getCenteredBlit(self.fontText.render(self.state.getTimeDivisionName(), Colors.TEXT)[0], LayoutWithClock.PERIOD_HEIGHT) )

    def createDynamicBlits(self, blitList) :
        Scoreboard.createDynamicBlits(self, blitList)
        blitList.append( self.layout.getMinutesBlit(self.insetSurface(self.minutesText.getValueAsSurface(self.state.getSeconds() // 60)))) 
        blitList.append( self.layout.getSecondsBlit(self.insetSurface(self.secondsText.getValueAsSurface(self.state.getSeconds() % 60)))) 
        #blitList.append( self.layout.getCenteredBlit(self.period.getValueAsSurface(self.state.getPeriod() ), LayoutWithClock.PERIOD_VALUE_HEIGHT ) )

        t = self.fontText.render(self.state.getTimeDivisionName() + ":", Colors.TEXT)[0]
        x = self.insetSurface(self.period.getValueAsSurface(self.state.getPeriod()  ))
        c = self.getCombinedSurface(t, x, 12)
        blitList.append(self.layout.getCenteredBlit(c, LayoutWithClock.PERIOD_HEIGHT))