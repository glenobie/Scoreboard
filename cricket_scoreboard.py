
from cricket_game_state import CricketGameState
from scoreboard import Scoreboard
from numericSurface import NumericSurface
from colors import Colors
from cricket_layout import CricketLayout
from scoreState import GameState
import pygame

class CricketScoreboard(Scoreboard):

    SPACING = 12


    def __init__(self, window):
        Scoreboard.__init__(self, window)

        self.state = CricketGameState()
        self.totalSurface = NumericSurface(self.fontScore, Colors.SCORE, 999)
        self.layout = CricketLayout(window)
        self.oversSurface = NumericSurface(self.fontSmallNumber, Colors.PERIOD, 999)
        self.batterSurface = NumericSurface(self.fontScore, Colors.SCORE, 999)
        self.wicketsSurface = NumericSurface(self.fontSmallNumber, Colors.PERIOD, 9)
        self.batterNumberSurface = NumericSurface(self.fontVerySmallNumber, Colors.SCORE, 19, False, 8, 8)
        self.lastWicketSurface = NumericSurface(self.fontSmallNumber, Colors.SCORE, 999 )
        self.lastInningsSurface = NumericSurface(self.fontSmallNumber, Colors.PERIOD, 999 )
        self.extrasSurface = NumericSurface(self.fontSmallNumber, Colors.SCORE, 99 )
        self.ballsSurface = NumericSurface(self.fontSmallNumber, Colors.PERIOD, 6 )
        self.createStaticBlits(self.staticBlitList)

    

    def createStaticBlits(self, blitList) :
        blitList.append( self.layout.getCenteredBlit( self.fontText.render("TOTAL", Colors.TEXT)[0] , CricketLayout.TOTAL_TITLE_HEIGHT) )
        blitList.append( self.layout.getCenteredBlit( self.fontSmallText.render("WICKETS", Colors.TEXT)[0] , CricketLayout.WICKETS_TITLE_HEIGHT) )
        blitList.append( self.layout.getCenteredBlit( self.fontSmallText.render("OVERS", Colors.TEXT)[0] , CricketLayout.BOWLING_TEAM_ROW_TITLE_HEIGHT) )
        blitList.append( self.layout.getLeftSideCenteredBlit( self.fontSmallText.render("EXTRAS", Colors.TEXT)[0] , CricketLayout.BATTING_TEAM_ROW2_TITLE_HEIGHT ) )
        blitList.append( self.layout.getRightSideCenteredBlit( self.fontSmallText.render("LAST WICKET", Colors.TEXT)[0] , CricketLayout.BATTING_TEAM_ROW2_TITLE_HEIGHT ))
        blitList.append( self.layout.getRightSideCenteredBlit( self.fontSmallText.render("LAST INNINGS", Colors.TEXT)[0] , CricketLayout.BOWLING_TEAM_ROW_TITLE_HEIGHT ))
        blitList.append( self.layout.getLeftSideCenteredBlit( self.fontSmallText.render("BALLS", Colors.TEXT)[0] , CricketLayout.BOWLING_TEAM_ROW_TITLE_HEIGHT ))
 
    def createDynamicBlits(self, blitList) :
        blitList.append( self.layout.getCenteredBlit(self.insetSurface(self.totalSurface.getValueAsSurface(self.state.getTotal())), CricketLayout.TOTAL_VALUE_HEIGHT ) )

        blitList.append(self.layout.getCenteredBlit ( self.insetSurface(self.wicketsSurface.getValueAsSurface(self.state.getWickets())), CricketLayout.WICKETS_VALUE_HEIGHT ))
        blitList.append(self.layout.getCenteredBlit ( self.insetSurface(self.oversSurface.getValueAsSurface(self.state.getOvers())), CricketLayout.BOWLING_TEAM_ROW_VALUE_HEIGHT ))
     
        t = self.fontSmallText.render("NO.", Colors.TEXT)[0]
        x = self.insetSurface(self.batterNumberSurface.getValueAsSurface(self.state.getLeftBatterNumber() ))
        c = self.getCombinedSurface(t, x, 12)
        blitList.append(self.layout.getLeftSideCenteredBlit(c, CricketLayout.BATTER_NUMBER_HEIGHT))

        t = self.fontSmallText.render("NO.", Colors.TEXT)[0]
        x = self.insetSurface(self.batterNumberSurface.getValueAsSurface(self.state.getRightBatterNumber() ))
        c = self.getCombinedSurface(t, x, 12)
        blitList.append(self.layout.getRightSideCenteredBlit(c, CricketLayout.BATTER_NUMBER_HEIGHT))

        blitList.append(self.layout.getLeftSideCenteredBlit ( self.insetSurface(self.totalSurface.getValueAsSurface(self.state.getLeftBatterRuns())), CricketLayout.BATTER_RUNS_HEIGHT ))
        blitList.append(self.layout.getRightSideCenteredBlit ( self.insetSurface(self.totalSurface.getValueAsSurface(self.state.getRightBatterRuns())), CricketLayout.BATTER_RUNS_HEIGHT ))

        blitList.append(self.layout.getRightSideCenteredBlit ( self.insetSurface(self.lastWicketSurface.getValueAsSurface(self.state.getLastWicket())), CricketLayout.BATTING_TEAM_ROW2_VALUE_HEIGHT ))
        blitList.append(self.layout.getRightSideCenteredBlit ( self.insetSurface(self.lastInningsSurface.getValueAsSurface(self.state.getLastInnings())), CricketLayout.BOWLING_TEAM_ROW_VALUE_HEIGHT ))

        blitList.append(self.layout.getLeftSideCenteredBlit ( self.insetSurface(self.extrasSurface.getValueAsSurface(self.state.getExtras())), CricketLayout.BATTING_TEAM_ROW2_VALUE_HEIGHT ))
        blitList.append(self.layout.getLeftSideCenteredBlit ( self.insetSurface(self.ballsSurface.getValueAsSurface(self.state.getBalls())), CricketLayout.BOWLING_TEAM_ROW_VALUE_HEIGHT ))

    def processKeyPress(self, event) :
        Scoreboard.processKeyPress(self, event)
        if event.key == pygame.K_q:
            if ( event.mod & pygame.KMOD_LSHIFT) :
                self.state.changeLeftBatter()
            else :
                self.state.incrementLeftBatterNumber()
        elif event.key == pygame.K_a:
            self.state.modifyExtras( event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_e:
            if ( event.mod & pygame.KMOD_LSHIFT) :
                self.state.changeRightBatter()
            else : 
                self.state.incrementRightBatterNumber()
        elif event.key == pygame.K_d:
            if ( event.mod & pygame.KMOD_LSHIFT) :
                self.state.changeSides()
            else :
                self.state.recordScore()
        elif event.key == pygame.K_s:
            self.state.incrementWickets()
        elif event.key == pygame.K_z:
            self.state.modifyLeftBatterRuns( event.mod & pygame.KMOD_LSHIFT)
        elif event.key == pygame.K_c:
            self.state.modifyRightBatterRuns( event.mod & pygame.KMOD_LSHIFT)



