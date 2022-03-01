
from tennis_game_state import TennisGameState
from scoreboard import Scoreboard
from numericSurface import NumericSurface
from colors import Colors
from tennis_layout import TennisLayout
from scoreState import GameState
import pygame

class TennisScoreboard(Scoreboard):

    
    def __init__(self, window):
        Scoreboard.__init__(self, window)

        self.state = TennisGameState()
        self.gameSurface = NumericSurface(self.fontScore, Colors.SCORE, 9)
        self.layout = TennisLayout(window)
        self.pointSurface = NumericSurface(self.fontScore, Colors.PERIOD, 99)
        self.createStaticBlits(self.staticBlitList)    


    def createStaticBlits(self, blitList) :
        x=0

    def createDynamicBlits(self, blitList) :
        t = self.fontText.render("Player 1", Colors.TEXT)[0]
        v = self.insetSurface(self.pointSurface.getValueAsSurface(self.state.getPoints(0)))
        blitList.append( ( self.getCombinedSurface(t, v, 20), (TennisLayout.COLS[1], TennisLayout.ROWS[0]) ) )
        t = self.fontText.render("Player 2", Colors.TEXT)[0]
        v = self.insetSurface(self.pointSurface.getValueAsSurface(self.state.getPoints(1)))
        blitList.append( ( self.getCombinedSurface(t, v, 20), (TennisLayout.COLS[1], TennisLayout.ROWS[1]) ) )

        index = 0
        for x in self.state.getPlayerSets(0) :
            blitList.append( ( self.insetSurface(self.gameSurface.getValueAsSurface(6)), (TennisLayout.COLS[index+2], TennisLayout.ROWS[0]) ) )
            index += 1

        index = 0  
        for x in self.state.getPlayerSets(1) :
            blitList.append( ( self.insetSurface(self.gameSurface.getValueAsSurface(6)), (TennisLayout.COLS[index+2], TennisLayout.ROWS[1]) ) )
            index += 1
 
    def processKeyPress(self, event) :
        Scoreboard.processKeyPress(self, event)
        if event.key == pygame.K_q:
            # cycle selected set
            x=0
        elif event.key == pygame.K_a:
            x=0
        elif event.key == pygame.K_e:
             # cycle selected set
            x=0
        elif event.key == pygame.K_d:
            x=0
        elif event.key == pygame.K_s:
            x=0
        elif event.key == pygame.K_z:
            self.state.modifyPoints(0,  event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_c:
            self.state.modifyPoints(1,  event.mod & pygame.KMOD_LSHIFT)
 


