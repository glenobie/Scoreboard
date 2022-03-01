
from bowling_game_state import BowlingGameState
from scoreboard import Scoreboard
from numericSurface import NumericSurface
from colors import Colors
from fonts import Fonts
from bowling_layout import BowlingLayout
from scoreState import GameState
import pygame

class BowlingScoreboard(Scoreboard):

    

    def __init__(self, window):
        Scoreboard.__init__(self, window)
        self.fontBall = pygame.freetype.Font(Fonts.DINGBAT_FILE, 20)
        self.layout = BowlingLayout(window)

        self.state = BowlingGameState()
        self.pinsSurface = NumericSurface(self.fontVerySmallNumber, Colors.SCORE, 9)
        self.scoreSurface = NumericSurface(self.fontSmallNumber, Colors.PERIOD, 999)

        self.bowlerUpSurface = NumericSurface(self.fontBall, Colors.CLOCK, 9)

        self.selectedFrame = 0

        self.createStaticBlits(self.staticBlitList)    


    def createStaticBlits(self, blitList) :
        x=0

    def addNameSurface(self, blitList, name, playerIndex, bowling) :
        if bowling : 
            ball = self.insetSurface(self.bowlerUpSurface.getValueAsSurface("T"))
        else :
            ball = self.insetSurface(self.bowlerUpSurface.getValueAsSurface(" "))
        n = self.fontText.render(name, Colors.TEXT)[0]
        blitList.append( ( self.getCombinedSurface(ball, n, 10), (BowlingLayout.COLS[0], BowlingLayout.ROWS[playerIndex]) ) )
    
    def addFrameSurfaces(self, blitList, playerIndex) :
        index = 0
        for x in self.state.getPlayerFrames(playerIndex) :
            if (index == self.selectedFrame) :
                self.scoreSurface.setColor(Colors.PERIOD)
            else :
                self.scoreSurface.setColor(Colors.SCORE)
        
            ball1 = self.insetSurface(self.pinsSurface.getValueAsSurface(self.state.getPins(playerIndex, index, 0)))
            ball2 = self.insetSurface(self.pinsSurface.getValueAsSurface(self.state.getPins(playerIndex, index, 1)))
            
            blitList.append( ( self.insetSurface(self.gameSurface.getValueAsSurface(self.state.getPlayerFrames(playerIndex)[index])), (BowlingLayout.COLS[index+1], BowlingLayout.ROWS[playerIndex]) ) )
            index += 1       

    def createDynamicBlits(self, blitList) :
        self.addNameSurface(blitList, "B1", 0, self.state.bowlers[0].bowling)
        self.addNameSurface(blitList, "B2", 1, self.state.bowlers[1].bowling)

        self.addFrameSurfaces(blitList, 0)
        self.addFrameSurfaces(blitList, 1)
 
 
    def cycleSelectedFrame(self, adj) :
        self.selectedFrame = (self.selectedSet + adj) % BowlingGameState.MAX_FRAMES


    def processKeyPress(self, event) :
        Scoreboard.processKeyPress(self, event)
        if event.key == pygame.K_q:
            self.cycleSelectedFrame(-1)
        elif event.key == pygame.K_a:
            self.state.modifyGames(0, self.selectedFrame, event.mod & pygame.KMOD_LSHIFT ) 
        elif event.key == pygame.K_e:
            self.cycleSelectedFrame(1)
        elif event.key == pygame.K_d:
            self.state.modifyGames(1, self.selectedFrame, event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_z:
            self.state.modifyPoints(0,  event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_c:
            self.state.modifyPoints(1,  event.mod & pygame.KMOD_LSHIFT)
 


