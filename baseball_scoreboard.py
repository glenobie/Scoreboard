
from baseball_game_state import BaseballGameState
from scoreboard import Scoreboard
from numericSurface import NumericSurface
from scoreboard import Colors
from baseball_layout import BaseballLayout
from scoreState import GameState
import pygame

class BaseballScoreboard(Scoreboard):
    def __init__(self, window):
        Scoreboard.__init__(self, window)

        self.state = BaseballGameState()
        self.scoreText = NumericSurface(self.fontScore, Colors.SCORE, 99)
        self.layout = BaseballLayout(window)
        self.hitsSurface = NumericSurface(self.fontSmallNumber, Colors.SCORE, 99)
        self.errorsSurface = NumericSurface(self.fontSmallNumber, Colors.SCORE, 99)
        self.createStaticBlits(self.staticBlitList)

    def createStaticBlits(self, blitList) :
        Scoreboard.createStaticBlits(self, blitList)
        blitList.append( self.layout.getLeftSideCenteredBlit( self.fontSmallText.render("HITS", Colors.TEXT)[0] , BaseballLayout.HITS_TITLE_HEIGHT) )
        blitList.append( self.layout.getRightSideCenteredBlit( self.fontSmallText.render("HITS", Colors.TEXT)[0] , BaseballLayout.HITS_TITLE_HEIGHT) )
        blitList.append( self.layout.getLeftSideCenteredBlit( self.fontSmallText.render("ERRORS", Colors.TEXT)[0] , BaseballLayout.ERRORS_TITLE_HEIGHT) )
        blitList.append( self.layout.getRightSideCenteredBlit( self.fontSmallText.render("ERRORS", Colors.TEXT)[0] , BaseballLayout.ERRORS_TITLE_HEIGHT) )

       
    def createDynamicBlits(self, blitList) :
        Scoreboard.createDynamicBlits(self, blitList)
        blitList.append( self.layout.getLeftSideCenteredBlit(self.hitsSurface.getValueAsSurface(self.state.getHits(GameState.HOME_INDEX) ), BaseballLayout.HITS_VALUE_HEIGHT ) )
        blitList.append( self.layout.getRightSideCenteredBlit(self.hitsSurface.getValueAsSurface(self.state.getHits(GameState.GUEST_INDEX) ), BaseballLayout.HITS_VALUE_HEIGHT ) )
        blitList.append( self.layout.getLeftSideCenteredBlit(self.errorsSurface.getValueAsSurface(self.state.getErrors(GameState.HOME_INDEX) ), BaseballLayout.ERRORS_VALUE_HEIGHT ) )
        blitList.append( self.layout.getRightSideCenteredBlit(self.errorsSurface.getValueAsSurface(self.state.getErrors(GameState.GUEST_INDEX) ), BaseballLayout.ERRORS_VALUE_HEIGHT ) )
                        
    def processKeyPress(self, event) :
        Scoreboard.processKeyPress(self, event)
        if event.key == pygame.K_a:
            self.state.modifyHits(GameState.HOME_INDEX, event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_q:
            self.state.modifyErrors(GameState.HOME_INDEX, event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_d:
            self.state.modifyHits(GameState.GUEST_INDEX, event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_e:
            self.state.modifyErrors(GameState.GUEST_INDEX, event.mod & pygame.KMOD_LSHIFT)


