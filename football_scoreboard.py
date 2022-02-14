from readline import insert_text
import pygame
from football_game_state import FootballGameState
from numericSurface import NumericSurface
from scoreboard import TimedScoreboard
from colors import Colors
from fonts import Fonts
from scoreState import GameState
from football_layout import FootballLayout

class FootballScoreboard(TimedScoreboard):
    def __init__(self, window):
        TimedScoreboard.__init__(self, window)
        self.state = FootballGameState()

        self.scoreText = NumericSurface(self.fontScore, Colors.SCORE, 99 )
        self.timeoutsSurface = NumericSurface(self.fontSmallNumber, Colors.SCORE, 5)
        self.minutesText = NumericSurface(self.fontClock, Colors.CLOCK, 20)
        self.downSurface = NumericSurface(self.fontSmallNumber, Colors.PERIOD, 9, False)
        self.ytgSurface = NumericSurface(self.fontSmallNumber, Colors.PERIOD, 99, False, 6)
        self.scrimmageSurface = NumericSurface(self.fontSmallNumber, Colors.SCORE, 99, False, 6)
        self.ltgSurface = NumericSurface(self.fontVerySmallNumber, Colors.PERIOD, 99, False, 4)


        self.layout = FootballLayout(window)
        self.createStaticBlits(self.staticBlitList)

   
    def createStaticBlits(self, blitList) :
        TimedScoreboard.createStaticBlits(self, blitList)
     #   blitList.append( self.layout.getLeftSideCenteredBlit( self.fontSmallText.render("TIMEOUTS", Colors.TEXT)[0] , FootballLayout.TIMEOUTS_TITLE_HEIGHT) )
     #   blitList.append( self.layout.getRightSideCenteredBlit( self.fontSmallText.render("TIMEOUTS", Colors.TEXT)[0] , FootballLayout.TIMEOUTS_TITLE_HEIGHT) )
 
       
    def createDynamicBlits(self, blitList) :
        TimedScoreboard.createDynamicBlits(self, blitList)
    #    blitList.append( self.layout.getLeftSideCenteredBlit(self.timeoutsSurface.getValueAsSurface(self.state.getTimeoutsTaken(GameState.HOME_INDEX) ), FootballLayout.TIMEOUTS_VALUE_HEIGHT ) )
    #    blitList.append( self.layout.getRightSideCenteredBlit(self.timeoutsSurface.getValueAsSurface(self.state.getTimeoutsTaken(GameState.GUEST_INDEX) ), FootballLayout.TIMEOUTS_VALUE_HEIGHT ) )

        t = self.fontText.render("DOWN:", Colors.TEXT)[0]
        x = self.insetSurface(self.downSurface.getValueAsSurface(self.state.getDown()  ))
        c = self.getCombinedSurface(t, x, 12)
        blitList.append(self.layout.getCenteredBlit(c, FootballLayout.DOWN_HEIGHT))
        t = self.fontText.render("YARDS TO GO:", Colors.TEXT)[0]
        toGo = self.state.getYardsToGain()
        if (toGo == FootballGameState.GOAL_TO_GO) :
            x = self.insetSurface( self.ytgSurface.getValueAsSurface("GO"))
        else :
            x = self.insetSurface( self.ytgSurface.getValueAsSurface(self.state.getYardsToGain()  ))
        c = self.getCombinedSurface(t, x, 12)
        blitList.append(self.layout.getCenteredBlit(c, FootballLayout.YTG_HEIGHT))
        t = self.fontSmallText.render("LINE TO GAIN:", Colors.TEXT)[0]
        x = self.insetSurface(self.ltgSurface.getValueAsSurface(self.state.getLineToGain()  ))
        c = self.getCombinedSurface(t, x, 12)
        blitList.append(self.layout.getCenteredBlit(c, FootballLayout.DISTANCE_HEIGHT))

        if (self.state.teamPossessingBall == GameState.HOME_INDEX) :
            blitList.append(self.layout.getLeftSideCenteredBlit(self.fontText.render("BALL ON", Colors.TEXT)[0], FootballLayout.BALL_TEXT_HEIGHT))
            blitList.append(self.layout.getLeftSideCenteredBlit(self.insetSurface(self.scrimmageSurface.getValueAsSurface(self.state.getLineOfScrimmage())), FootballLayout.BALL_VALUE_HEIGHT  ))
        else :
            blitList.append(self.layout.getRightSideCenteredBlit(self.fontText.render("BALL ON", Colors.TEXT)[0], FootballLayout.BALL_TEXT_HEIGHT))
            blitList.append(self.layout.getRightSideCenteredBlit(self.insetSurface(self.scrimmageSurface.getValueAsSurface(self.state.getLineOfScrimmage())), FootballLayout.BALL_VALUE_HEIGHT  ))


    def processKeyPress(self, event) :
        TimedScoreboard.processKeyPress(self, event)
        if event.key == pygame.K_a:
            self.state.modifyLineOfScrimmage(1,  event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_q:
            self.state.modifyLineOfScrimmage(10,  event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_d:
            if (event.mod & pygame.KMOD_LSHIFT) :
                self.state.resetDownAndDistance()
            else:
                self.state.modifyDown()
        elif event.key == pygame.K_e:
            self.state.changePossessingTeam()



