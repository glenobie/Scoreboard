import pygame
from football_game_state import FootballGameState
from numericSurface import NumericSurface
from scoreboard import TimedScoreboard
from scoreboard import Colors
from scoreboard import Fonts
from scoreState import GameState
from football_layout import FootballLayout

class FootballScoreboard(TimedScoreboard):
    def __init__(self, window):
        TimedScoreboard.__init__(self, window)
        self.state = FootballGameState()
        self.scoreText = NumericSurface(self.fontScore, Colors.SCORE, 99 )
        self.timeoutsSurface = NumericSurface(self.fontSmallNumber, Colors.SCORE, 5)

        self.layout = FootballLayout(window)
        self.createStaticBlits(self.staticBlitList)

   
    def createStaticBlits(self, blitList) :
        TimedScoreboard.createStaticBlits(self, blitList)
        blitList.append( self.layout.getLeftSideCenteredBlit( self.fontSmallText.render("TIMEOUTS", Colors.TEXT)[0] , FootballLayout.TIMEOUTS_TITLE_HEIGHT) )
        blitList.append( self.layout.getRightSideCenteredBlit( self.fontSmallText.render("TIMEOUTS", Colors.TEXT)[0] , FootballLayout.TIMEOUTS_TITLE_HEIGHT) )

       
    def createDynamicBlits(self, blitList) :
        TimedScoreboard.createDynamicBlits(self, blitList)
        blitList.append( self.layout.getLeftSideCenteredBlit(self.timeoutsSurface.getValueAsSurface(self.state.getTimeoutsTaken(GameState.HOME_INDEX) ), FootballLayout.TIMEOUTS_VALUE_HEIGHT ) )
        blitList.append( self.layout.getRightSideCenteredBlit(self.timeoutsSurface.getValueAsSurface(self.state.getTimeoutsTaken(GameState.GUEST_INDEX) ), FootballLayout.TIMEOUTS_VALUE_HEIGHT ) )


    def processKeyPress(self, event) :
        TimedScoreboard.processKeyPress(self, event)
        if event.key == pygame.K_a:
            #self.state.modifyLineOfScrimmageTeamFouls(GameState.HOME_INDEX, event.mod & pygame.KMOD_LSHIFT)
            x=0
        elif event.key == pygame.K_q:
            self.state.modifyTimeoutsTaken(GameState.HOME_INDEX, event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_d:
           # self.state.modifyTeamFouls(GameState.GUEST_INDEX, event.mod & pygame.KMOD_LSHIFT)
           x=0
        elif event.key == pygame.K_e:
            self.state.modifyTimeoutsTaken(GameState.GUEST_INDEX, event.mod & pygame.KMOD_LSHIFT)



