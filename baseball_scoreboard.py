
from telnetlib import GA
from baseball_game_state import BaseballGameState
from scoreboard import Scoreboard
from numericSurface import NumericSurface
from colors import Colors
from baseball_layout import BaseballLayout
from scoreState import GameState
import pygame

class BaseballScoreboard(Scoreboard):

    SPACING = 12

    def __init__(self, window):
        Scoreboard.__init__(self, window)

        self.state = BaseballGameState()
        self.scoreText = NumericSurface(self.fontScore, Colors.SCORE, 99)
        self.layout = BaseballLayout(window)
        self.hitsSurface = NumericSurface(self.fontSmallNumber, Colors.SCORE, 99)
        self.errorsSurface = NumericSurface(self.fontSmallNumber, Colors.SCORE, 99)
        self.outSurface = NumericSurface(self.fontSmallNumber, Colors.PERIOD, 2)
        self.inningNumberSurface = NumericSurface(self.fontScore, Colors.PERIOD, 99)
        self.halfInningSize = self.fontVerySmallNumber.render("BTM")[0].get_size()
        self.createStaticBlits(self.staticBlitList)

    def createInningSurface(self) :
        n = self.inningNumberSurface.getValueAsSurface(self.state.getInning())
        h = pygame.Surface( (self.halfInningSize[0], self.halfInningSize[1] * 2 + BaseballScoreboard.SPACING ) )
       
        y = 0
        if self.state.getTeamAtBat() == GameState.HOME_INDEX :
            y = self.halfInningSize[1] + BaseballScoreboard.SPACING
        h.blit(self.fontVerySmallNumber.render(self.state.getHalfInning(), Colors.PERIOD)[0], (0, y))
        c = self.getCombinedSurface(h, n, 12)
        return c

    def createStaticBlits(self, blitList) :
        Scoreboard.createStaticBlits(self, blitList)
        blitList.append( self.layout.getLeftSideCenteredBlit( self.fontSmallText.render("HITS", Colors.TEXT)[0] , BaseballLayout.HITS_TITLE_HEIGHT) )
        blitList.append( self.layout.getRightSideCenteredBlit( self.fontSmallText.render("HITS", Colors.TEXT)[0] , BaseballLayout.HITS_TITLE_HEIGHT) )
        blitList.append( self.layout.getLeftSideCenteredBlit( self.fontSmallText.render("ERRORS", Colors.TEXT)[0] , BaseballLayout.ERRORS_TITLE_HEIGHT) )
        blitList.append( self.layout.getRightSideCenteredBlit( self.fontSmallText.render("ERRORS", Colors.TEXT)[0] , BaseballLayout.ERRORS_TITLE_HEIGHT) )
        blitList.append( self.layout.getCenteredBlit( self.fontText.render("INNING", Colors.TEXT)[0] , BaseballLayout.INNING_TITLE_HEIGHT) )
        blitList.append( self.layout.getCenteredBlit( self.fontText.render("OUTS", Colors.TEXT)[0] , BaseballLayout.OUTS_TITLE_HEIGHT) )
       
    def createDynamicBlits(self, blitList) :
        Scoreboard.createDynamicBlits(self, blitList)
        blitList.append( self.layout.getLeftSideCenteredBlit(self.hitsSurface.getValueAsSurface(self.state.getHits(GameState.HOME_INDEX) ), BaseballLayout.HITS_VALUE_HEIGHT ) )
        blitList.append( self.layout.getRightSideCenteredBlit(self.hitsSurface.getValueAsSurface(self.state.getHits(GameState.GUEST_INDEX) ), BaseballLayout.HITS_VALUE_HEIGHT ) )
        blitList.append( self.layout.getLeftSideCenteredBlit(self.errorsSurface.getValueAsSurface(self.state.getErrors(GameState.HOME_INDEX) ), BaseballLayout.ERRORS_VALUE_HEIGHT ) )
        blitList.append( self.layout.getRightSideCenteredBlit(self.errorsSurface.getValueAsSurface(self.state.getErrors(GameState.GUEST_INDEX) ), BaseballLayout.ERRORS_VALUE_HEIGHT ) )
        blitList.append( self.layout.getCenteredBlit(self.outSurface.getValueAsSurface(self.state.getOuts()), BaseballLayout.OUTS_VALUE_HEIGHT ) )

        blitList.append(self.layout.getCenteredBlit(self.createInningSurface(), BaseballLayout.INNING_BOTTOM_HALF_HEIGHT))


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
        elif event.key == pygame.K_s:
            self.state.modifyOuts()



