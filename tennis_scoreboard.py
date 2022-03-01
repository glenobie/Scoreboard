
from tennis_game_state import TennisGameState
from scoreboard import Scoreboard
from numericSurface import NumericSurface
from colors import Colors
from tennis_layout import TennisLayout
from scoreState import GameState
import pygame

class TennisScoreboard(Scoreboard):

    NUM_SETS = 5

    def __init__(self, window):
        Scoreboard.__init__(self, window)

        self.state = TennisGameState()
        self.gameSurface = NumericSurface(self.fontScore, Colors.SCORE, 9)
        self.layout = TennisLayout(window)
        self.pointSurface = NumericSurface(self.fontScore, Colors.PERIOD, 99)

        self.selectedSet = 0

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

        self.addSetSurfaces(blitList, 0)
        self.addSetSurfaces(blitList, 1)
 
    def addSetSurfaces(self, blitList, playerIndex) :
        index = 0
        for x in self.state.getPlayerSets(playerIndex) :
            if (index == self.selectedSet) :
                self.gameSurface.setColor(Colors.PERIOD)
            else :
                self.gameSurface.setColor(Colors.SCORE)
            blitList.append( ( self.insetSurface(self.gameSurface.getValueAsSurface(self.state.getPlayerSets(playerIndex)[index])), (TennisLayout.COLS[index+2], TennisLayout.ROWS[playerIndex]) ) )
            index += 1

 
    def cycleSelectedSet(self, adj) :
        self.selectedSet = (self.selectedSet + adj) % TennisScoreboard.NUM_SETS


    def processKeyPress(self, event) :
        Scoreboard.processKeyPress(self, event)
        if event.key == pygame.K_q:
            self.cycleSelectedSet(-1)
        elif event.key == pygame.K_a:
            self.state.modifyGames(0, self.selectedSet, event.mod & pygame.KMOD_LSHIFT ) 
        elif event.key == pygame.K_e:
            self.cycleSelectedSet(1)
        elif event.key == pygame.K_d:
             self.state.modifyGames(1, self.selectedSet, event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_s:
            x=0
        elif event.key == pygame.K_z:
            self.state.modifyPoints(0,  event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_c:
            self.state.modifyPoints(1,  event.mod & pygame.KMOD_LSHIFT)
 


