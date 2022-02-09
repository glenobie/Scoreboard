
from telnetlib import GA
from basketball_game_state import BasketballGameState
from numericSurface import NumericSurface
from scoreboard import TimedScoreboard
from scoreboard import Colors
from basketball_layout import BasketballLayout
from scoreState import GameState
import pygame

class BasketballScoreboard(TimedScoreboard):
    def __init__(self, window):
        TimedScoreboard.__init__(self, window)

        self.state = BasketballGameState()
        self.scoreText = NumericSurface(self.fontScore, Colors.SCORE, 199)
        self.layout = BasketballLayout(window)
        self.timeoutsSurface = NumericSurface(self.fontSmallNumber, Colors.SCORE, 9)
        self.teamFoulsSurface = NumericSurface(self.fontSmallNumber, Colors.SCORE, 19)
        self.createStaticBlits(self.staticBlitList)

    def createStaticBlits(self, blitList) :
        TimedScoreboard.createStaticBlits(self, blitList)
        blitList.append( self.layout.getLeftSideCenteredBlit( self.fontSmallText.render("TEAM FOULS", Colors.TEXT)[0] , BasketballLayout.TEAM_FOULS_TITLE_HEIGHT) )
        blitList.append( self.layout.getRightSideCenteredBlit( self.fontSmallText.render("TEAM FOULS", Colors.TEXT)[0] , BasketballLayout.TEAM_FOULS_TITLE_HEIGHT) )
        blitList.append( self.layout.getLeftSideCenteredBlit( self.fontSmallText.render("TIMEOUTS", Colors.TEXT)[0] , BasketballLayout.TIMEOUTS_TITLE_HEIGHT) )
        blitList.append( self.layout.getRightSideCenteredBlit( self.fontSmallText.render("TIMEOUTS", Colors.TEXT)[0] , BasketballLayout.TIMEOUTS_TITLE_HEIGHT) )

       
    def createDynamicBlits(self, blitList) :
        TimedScoreboard.createDynamicBlits(self, blitList)
        blitList.append( self.layout.getLeftSideCenteredBlit(self.teamFoulsSurface.getValueAsSurface(self.state.getTeamFouls(GameState.HOME_INDEX) ), BasketballLayout.TEAM_FOULS_VALUE_HEIGHT ) )
        blitList.append( self.layout.getLeftSideCenteredBlit(self.timeoutsSurface.getValueAsSurface(self.state.getTimeoutsTaken(GameState.HOME_INDEX) ), BasketballLayout.TIMEOUTS_VALUE_HEIGHT ) )
        blitList.append( self.layout.getRightSideCenteredBlit(self.teamFoulsSurface.getValueAsSurface(self.state.getTeamFouls(GameState.GUEST_INDEX) ), BasketballLayout.TEAM_FOULS_VALUE_HEIGHT ) )
        blitList.append( self.layout.getRightSideCenteredBlit(self.timeoutsSurface.getValueAsSurface(self.state.getTimeoutsTaken(GameState.GUEST_INDEX) ), BasketballLayout.TIMEOUTS_VALUE_HEIGHT ) )
                        
    def processKeyPress(self, event) :
        TimedScoreboard.processKeyPress(self, event)
        if event.key == pygame.K_a:
            self.state.modifyTeamFouls(GameState.HOME_INDEX, event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_q:
            self.state.modifyTimeoutsTaken(GameState.HOME_INDEX, event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_d:
            self.state.modifyTeamFouls(GameState.GUEST_INDEX, event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_e:
            self.state.modifyTimeoutsTaken(GameState.GUEST_INDEX, event.mod & pygame.KMOD_LSHIFT)


