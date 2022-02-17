
from telnetlib import GA
from boxing_game_state import BoxingGameState
from numericSurface import NumericSurface
from scoreboard import TimedScoreboard
from colors import Colors
from boxing_layout import BoxingLayout
from scoreState import GameState
import pygame

class BoxingScoreboard(TimedScoreboard):
    def __init__(self, window):
        TimedScoreboard.__init__(self, window, "Red", "Blue")

        self.state = BoxingGameState()
        self.scoreText = NumericSurface(self.fontScore, Colors.SCORE, 99)
        self.layout = BoxingLayout(window)
        self.minutesText = NumericSurface(self.fontClock, Colors.CLOCK, 20)
        

        self.enduranceSurface = NumericSurface(self.fontSmallNumber, Colors.SCORE, 999)
        self.period = NumericSurface(self.fontSmallNumber, Colors.PERIOD, 19, False)

        self.createStaticBlits(self.staticBlitList)

    def createStaticBlits(self, blitList) :
        TimedScoreboard.createStaticBlits(self, blitList)
        blitList.append( self.layout.getLeftSideCenteredBlit( self.fontSmallText.render("ENDURANCE", Colors.TEXT)[0] , BoxingLayout.TEAM_FOULS_TITLE_HEIGHT) )
        blitList.append( self.layout.getRightSideCenteredBlit( self.fontSmallText.render("ENDURANCE", Colors.TEXT)[0] , BoxingLayout.TEAM_FOULS_TITLE_HEIGHT) )
        #blitList.append( self.layout.getLeftSideCenteredBlit( self.fontSmallText.render("TIMEOUTS", Colors.TEXT)[0] , BoxingLayout.TIMEOUTS_TITLE_HEIGHT) )
        #blitList.append( self.layout.getRightSideCenteredBlit( self.fontSmallText.render("TIMEOUTS", Colors.TEXT)[0] , BoxingLayout.TIMEOUTS_TITLE_HEIGHT) )

       
    def createDynamicBlits(self, blitList) :
        TimedScoreboard.createDynamicBlits(self, blitList)
        blitList.append( self.layout.getLeftSideCenteredBlit(self.insetSurface(self.enduranceSurface.getValueAsSurface(self.state.getEndurance(GameState.HOME_INDEX) )), BoxingLayout.TEAM_FOULS_VALUE_HEIGHT ) )
       # blitList.append( self.layout.getLeftSideCenteredBlit(self.insetSurface(self.timeoutsSurface.getValueAsSurface(self.state.getTimeoutsTaken(GameState.HOME_INDEX)) ), BoxingLayout.TIMEOUTS_VALUE_HEIGHT ) )
        blitList.append( self.layout.getRightSideCenteredBlit(self.insetSurface(self.enduranceSurface.getValueAsSurface(self.state.getEndurance(GameState.GUEST_INDEX) )), BoxingLayout.TEAM_FOULS_VALUE_HEIGHT ) )
        #blitList.append( self.layout.getRightSideCenteredBlit(self.insetSurface(self.timeoutsSurface.getValueAsSurface(self.state.getTimeoutsTaken(GameState.GUEST_INDEX)) ), BoxingLayout.TIMEOUTS_VALUE_HEIGHT ) )
                        
    def processKeyPress(self, event) :
        TimedScoreboard.processKeyPress(self, event)
        if event.key == pygame.K_a:
            self.state.modifyEndurance(GameState.HOME_INDEX, event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_q:
            self.state.resetRound()
        elif event.key == pygame.K_d:
            self.state.modifyEndurance(GameState.GUEST_INDEX, event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_e:
            self.state.resetRound()


