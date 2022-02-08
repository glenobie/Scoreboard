import pygame
from layout import HockeyLayout, Layout, LayoutWithClock
from hockey_game_state import HockeyGameState
from numericSurface import NumericSurface
from scoreboard import TimedScoreboard
from scoreboard import Colors
from scoreboard import Fonts

class HockeyScoreboard(TimedScoreboard):
    def __init__(self, window):
        TimedScoreboard.__init__(self, window)
        self.penaltyMinutes = NumericSurface(self.fontSmallNumber, Colors.CLOCK, 9)
        self.penaltySeconds = NumericSurface(self.fontSmallNumber, Colors.CLOCK, 99, True)
        self.state = HockeyGameState()
        self.scoreText = NumericSurface(self.fontScore, Colors.SCORE, self.state.getMaxScore() )

        self.layout = HockeyLayout(window)
        self.createStaticBlits(self.staticBlitList)
        


    def processKeyPress(self, event) :
        TimedScoreboard.processKeyPress(self, event)
        if event.key == pygame.K_a:
            self.state.modifyPenaltyClock(HockeyGameState.HOME_INDEX, 0)
        elif event.key == pygame.K_q:
            self.state.modifyPenaltyClock(HockeyGameState.HOME_INDEX, 1)
        elif event.key == pygame.K_d:
            self.state.modifyPenaltyClock(HockeyGameState.GUEST_INDEX, 0)
        elif event.key == pygame.K_e:
            self.state.modifyPenaltyClock(HockeyGameState.GUEST_INDEX, 1)

    def createStaticBlits(self, blitList) :
        TimedScoreboard.createStaticBlits(self, blitList)
        blitList.append( self.layout.getLeftSideCenteredBlit( self.fontText.render("PENALTY", Colors.TEXT)[0] , HockeyLayout.PENALTY_1_HEIGHT) )
        blitList.append( self.layout.getRightSideCenteredBlit( self.fontText.render("PENALTY", Colors.TEXT)[0] , HockeyLayout.PENALTY_1_HEIGHT) )

        blitList.append( self.layout.getLeftSideCenteredBlit( self.fontText.render("PENALTY", Colors.TEXT)[0] , HockeyLayout.PENALTY_2_HEIGHT) )
        blitList.append( self.layout.getRightSideCenteredBlit( self.fontText.render("PENALTY", Colors.TEXT)[0] , HockeyLayout.PENALTY_2_HEIGHT) )
       
        blitList.append( self.layout.getLeftPenaltyColonBlit( self.fontSmallNumber.render(":", Colors.CLOCK)[0] , HockeyLayout.PENALTY_1_COLON_HEIGHT) )
        blitList.append( self.layout.getLeftPenaltyColonBlit( self.fontSmallNumber.render(":", Colors.CLOCK)[0] , HockeyLayout.PENALTY_2_COLON_HEIGHT) )
        blitList.append( self.layout.getRightPenaltyColonBlit( self.fontSmallNumber.render(":", Colors.CLOCK)[0] , HockeyLayout.PENALTY_1_COLON_HEIGHT) )
        blitList.append( self.layout.getRightPenaltyColonBlit( self.fontSmallNumber.render(":", Colors.CLOCK)[0] , HockeyLayout.PENALTY_2_COLON_HEIGHT) )
 
      
    def createDynamicBlits(self, blitList) :
        TimedScoreboard.createDynamicBlits(self, blitList)

        blitList.append( self.layout.getLeftPenaltyMinutesBlit(self.penaltyMinutes.getValueAsSurface(self.state.getPenaltySeconds(HockeyGameState.HOME_INDEX, 0) // 60), HockeyLayout.PENALTY_1_TIME_HEIGHT)) 
        blitList.append( self.layout.getLeftPenaltySecondsBlit(self.penaltySeconds.getValueAsSurface(self.state.getPenaltySeconds(HockeyGameState.HOME_INDEX, 0) % 60), HockeyLayout.PENALTY_1_TIME_HEIGHT)) 

        blitList.append( self.layout.getLeftPenaltyMinutesBlit(self.penaltyMinutes.getValueAsSurface(self.state.getPenaltySeconds(HockeyGameState.HOME_INDEX, 1) // 60), HockeyLayout.PENALTY_2_TIME_HEIGHT)) 
        blitList.append( self.layout.getLeftPenaltySecondsBlit(self.penaltySeconds.getValueAsSurface(self.state.getPenaltySeconds(HockeyGameState.HOME_INDEX, 1) % 60), HockeyLayout.PENALTY_2_TIME_HEIGHT)) 

        blitList.append( self.layout.getRightPenaltyMinutesBlit(self.penaltyMinutes.getValueAsSurface(self.state.getPenaltySeconds(HockeyGameState.GUEST_INDEX, 0) // 60), HockeyLayout.PENALTY_1_TIME_HEIGHT)) 
        blitList.append( self.layout.getRightPenaltySecondsBlit(self.penaltySeconds.getValueAsSurface(self.state.getPenaltySeconds(HockeyGameState.GUEST_INDEX, 0) % 60), HockeyLayout.PENALTY_1_TIME_HEIGHT)) 

        blitList.append( self.layout.getRightPenaltyMinutesBlit(self.penaltyMinutes.getValueAsSurface(self.state.getPenaltySeconds(HockeyGameState.GUEST_INDEX, 1) // 60), HockeyLayout.PENALTY_2_TIME_HEIGHT)) 
        blitList.append( self.layout.getRightPenaltySecondsBlit(self.penaltySeconds.getValueAsSurface(self.state.getPenaltySeconds(HockeyGameState.GUEST_INDEX, 1) % 60), HockeyLayout.PENALTY_2_TIME_HEIGHT)) 
    # self.period.writeToSurface(self.window, self.state.getPeriod(), HockeyLayout.PERIOD_VALUE)


