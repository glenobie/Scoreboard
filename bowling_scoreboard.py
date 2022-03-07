
from bowling_game_state import BowlingGameState
from scoreboard import Scoreboard
from numericSurface import NumericSurface
from colors import Colors
from fonts import Fonts
from bowling_layout import BowlingLayout
import pygame

class BowlingScoreboard(Scoreboard):

    

    def __init__(self, window):
        Scoreboard.__init__(self, window)
        #self.fontBall = pygame.freetype.Font(Fonts.DINGBAT_FILE, 20)
        self.layout = BowlingLayout(window)

        self.state = BowlingGameState()
        self.fontPins = pygame.freetype.Font(Fonts.NUMERIC_FILE, BowlingLayout.PINS_FONT_SIZE)
        self.fontScore = pygame.freetype.Font(Fonts.NUMERIC_FILE, BowlingLayout.SCORE_FONT_SIZE)
        self.pinsSurface = NumericSurface(self.fontPins, Colors.SCORE, 9)
        self.scoreSurface = NumericSurface(self.fontScore, Colors.PERIOD, 999, False, 2)

        #self.bowlerUpSurface = NumericSurface(self.fontBall, Colors.CLOCK, 9)

        self.selectedFrame = 0

        self.createStaticBlits(self.staticBlitList)    


    def createStaticBlits(self, blitList) :
        x = 0

    def getFramesSurface(self, playerIndex) :
        s = pygame.Surface((740,90))
        s.fill(Colors.BACKGROUND)
        index = 0
        offset = 2
        x=y=0
        bowler = self.state.bowlers[playerIndex]
        for frame in bowler.frames :
            if (index == self.selectedFrame) :
                self.scoreSurface.setColor(Colors.PERIOD)
                self.pinsSurface.setColor(Colors.PERIOD)
            else :
                self.scoreSurface.setColor(Colors.SCORE)
                self.pinsSurface.setColor(Colors.SCORE)
        
            ball1 = self.insetSurface(self.pinsSurface.getValueAsSurface(frame.getDisplay(0)))
            ball2 = self.insetSurface(self.pinsSurface.getValueAsSurface(frame.getDisplay(1)))
            twoBalls = self.getCombinedSurface(ball1, ball2, 2)
            if (frame.isTenth()) :
                ball3 = self.insetSurface(self.pinsSurface.getValueAsSurface(frame.getDisplay(2)))
                threeBalls = self.getCombinedSurface(twoBalls, ball3, 2) 
                s.blit(threeBalls, (x+offset,y+offset))
            else :
                s.blit( twoBalls, (x+offset, y+offset) ) 
            
            s.blit( self.insetSurface(self.scoreSurface.getValueAsSurface(bowler.getScore(index+1))), (x+offset, y + 42+offset) )
            if (index < 9) :
                pygame.draw.rect(s, Colors.FRAME, (x, y, BowlingLayout.FRAME_WIDTH, BowlingLayout.FRAME_HEIGHT), 1)
            else :
                pygame.draw.rect(s, Colors.FRAME, (x, y, BowlingLayout.FRAME_WIDTH + BowlingLayout.FRAME_WIDTH / 2, BowlingLayout.FRAME_HEIGHT), 1)
            x += BowlingLayout.FRAME_SPACING + offset
            index += 1
        return s

    def createDynamicBlits(self, blitList) :

        x = 90
        y1 = BowlingLayout.ROW1 - 50
        y2 = BowlingLayout.ROW2 - 50
        f=1
        for i in range(BowlingGameState.MAX_FRAMES) :
            c = Colors.TEXT
            if i == self.selectedFrame : c = Colors.PERIOD
            s = self.fontSmallText.render(str(f), c)[0] 
            blitList.append( ( s, (x,y1) ) )
            blitList.append( ( s, (x,y2) ) )
            x += BowlingLayout.FRAME_SPACING + 2
            f += 1

        f = self.getFramesSurface(0)
        n = self.fontText.render("B1", Colors.TEXT)[0]
        blitList.append( ( self.getCombinedSurface(n, f,  10), (BowlingLayout.LEFT_MARGIN, BowlingLayout.ROW1) ) )
    
        f = self.getFramesSurface(1)
        n = self.fontText.render("B2", Colors.TEXT)[0]
        blitList.append( ( self.getCombinedSurface(n, f,  10), (BowlingLayout.LEFT_MARGIN, BowlingLayout.ROW2) ) )
 
    def cycleSelectedFrame(self, adj) :
        self.selectedFrame = (self.selectedFrame + adj) % BowlingGameState.MAX_FRAMES

    def processKeyPress(self, event) :
        Scoreboard.processKeyPress(self, event)
        if event.key == pygame.K_q:
            if event.mod & pygame.KMOD_LSHIFT :
                self.state.modifyPins(0, 9, 2, False)
            else :
                self.cycleSelectedFrame(-1)
        elif event.key == pygame.K_e:
            if event.mod & pygame.KMOD_LSHIFT :
                self.state.modifyPins(1, 9, 2, False)
            else :
                self.cycleSelectedFrame(1)
        elif event.key == pygame.K_a:
            self.state.modifyPins(0, self.selectedFrame, 0, event.mod & pygame.KMOD_LSHIFT ) 
        elif event.key == pygame.K_d:
            self.state.modifyPins(0, self.selectedFrame, 1, event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_z:
            self.state.modifyPins(1,  self.selectedFrame, 0, event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_c:
            self.state.modifyPins(1,  self.selectedFrame, 1, event.mod & pygame.KMOD_LSHIFT)
 


