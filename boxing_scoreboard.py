
from telnetlib import GA
from boxing_game_state import BoxingGameState
from numericSurface import NumericSurface
from scoreboard import TimedScoreboard
from colors import Colors
from boxing_layout import BoxingLayout
from scoreState import GameState
from layout import Layout, LayoutWithClock
import pygame

class BoxingScoreboard(TimedScoreboard):
    def __init__(self, window):
        TimedScoreboard.__init__(self, window, "Red", "Blue")

        self.state = BoxingGameState()
        self.scoreRed = NumericSurface(self.fontScore, Colors.SCORE, 99)
        self.scoreBlue = NumericSurface(self.fontScore, Colors.BLUE, 99)
        self.layout = BoxingLayout(window)
        self.minutesText = NumericSurface(self.fontClock, Colors.CLOCK, 20)
        

        self.enduranceRed = NumericSurface(self.fontSmallNumber, Colors.SCORE, 999)
        self.enduranceBlue = NumericSurface(self.fontSmallNumber, Colors.BLUE, 999)
        self.period = NumericSurface(self.fontSmallNumber, Colors.CLOCK, 19, False)

        self.createStaticBlits(self.staticBlitList)

    def createStaticBlits(self, blitList) :
        TimedScoreboard.createStaticBlits(self, blitList)
        blitList.append( self.layout.getLeftSideCenteredBlit( self.fontSmallText.render("ENDURANCE", Colors.TEXT)[0] , BoxingLayout.ENDURANCE_TITLE_HEIGHT) )
        blitList.append( self.layout.getRightSideCenteredBlit( self.fontSmallText.render("ENDURANCE", Colors.TEXT)[0] , BoxingLayout.ENDURANCE_TITLE_HEIGHT) )
        blitList.append( self.layout.getLeftSideCenteredBlit( self.fontSmallText.render("TKO POINTS", Colors.TEXT)[0] , BoxingLayout.TKO_TITLE_HEIGHT) )
        blitList.append( self.layout.getRightSideCenteredBlit( self.fontSmallText.render("TKO POINTS", Colors.TEXT)[0] , BoxingLayout.TKO_TITLE_HEIGHT) )

       
    def createDynamicBlits(self, blitList) :
        blitList.append( self.layout.getLeftSideCenteredBlit(self.insetSurface(self.scoreRed.getValueAsSurface(self.state.getHomeScore())), Layout.SCORE_HEIGHT)) 
        blitList.append( self.layout.getRightSideCenteredBlit(self.insetSurface(self.scoreBlue.getValueAsSurface(self.state.getGuestScore())), Layout.SCORE_HEIGHT)) 

        blitList.append( self.layout.getMinutesBlit(self.insetSurface(self.minutesText.getValueAsSurface(self.state.getSeconds() // 60)))) 
        blitList.append( self.layout.getSecondsBlit(self.insetSurface(self.secondsText.getValueAsSurface(self.state.getSeconds() % 60)))) 
        blitList.append( self.layout.getLeftSideCenteredBlit(self.insetSurface(self.enduranceRed.getValueAsSurface(self.state.getEndurance(GameState.HOME_INDEX) )), BoxingLayout.ENDURANCE_VALUE_HEIGHT ) )
        blitList.append( self.layout.getRightSideCenteredBlit(self.insetSurface(self.enduranceBlue.getValueAsSurface(self.state.getEndurance(GameState.GUEST_INDEX) )), BoxingLayout.ENDURANCE_VALUE_HEIGHT ) )
        blitList.append( self.layout.getLeftSideCenteredBlit(self.insetSurface(self.enduranceRed.getValueAsSurface(self.state.getTkoPoints(GameState.HOME_INDEX) )), BoxingLayout.TKO_VALUE_HEIGHT ) )
        blitList.append( self.layout.getRightSideCenteredBlit(self.insetSurface(self.enduranceBlue.getValueAsSurface(self.state.getTkoPoints(GameState.GUEST_INDEX) )), BoxingLayout.TKO_VALUE_HEIGHT ) )

        t = self.fontText.render(self.state.getTimeDivisionName() + ":", Colors.TEXT)[0]
        x = self.insetSurface(self.period.getValueAsSurface(self.state.getPeriod()  ))
        c = self.getCombinedSurface(t, x, 12)
        blitList.append(self.layout.getCenteredBlit(c, LayoutWithClock.PERIOD_HEIGHT))

    def processKeyPress(self, event) :
        TimedScoreboard.processKeyPress(self, event)
        if event.key == pygame.K_a:
            self.state.modifyEndurance(GameState.HOME_INDEX, event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_q:
            self.state.modifyTkoPoints(GameState.HOME_INDEX, event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_d:
            self.state.modifyEndurance(GameState.GUEST_INDEX, event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_e:
            self.state.modifyTkoPoints(GameState.GUEST_INDEX, event.mod & pygame.KMOD_LSHIFT)
            


