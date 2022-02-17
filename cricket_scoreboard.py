
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
        self.scoreText = NumericSurface(self.fontScore, Colors.SCORE, 99)
        self.layout = CricketLayout(window)
        self.hitsSurface = NumericSurface(self.fontSmallNumber, Colors.SCORE, 99)
        self.errorsSurface = NumericSurface(self.fontSmallNumber, Colors.SCORE, 99)
        self.outSurface = NumericSurface(self.fontSmallNumber, Colors.PERIOD, 2)
        self.inningNumberSurface = NumericSurface(self.fontScore, Colors.PERIOD, 99, False, 8, 8)
        self.halfInningSize = self.fontVerySmallNumber.render("BTM")[0].get_size()
        self.createStaticBlits(self.staticBlitList)

    def createInningSurface(self) :
        n = self.inningNumberSurface.getValueAsSurface(self.state.getInning())
        h = pygame.Surface( (self.halfInningSize[0] + Scoreboard.OUTLINE_SPACING, 
                        self.halfInningSize[1] * 2 + CricketScoreboard.SPACING + Scoreboard.OUTLINE_SPACING*2) )
        h.fill(Colors.BACKGROUND)
        y = Scoreboard.OUTLINE_SPACING
        if self.state.getTeamAtBat() == GameState.HOME_INDEX :
            y += self.halfInningSize[1] + CricketScoreboard.SPACING 
        h.blit(self.fontVerySmallNumber.render(self.state.getHalfInning(), Colors.PERIOD)[0], (Scoreboard.OUTLINE_SPACING, y))
        c = self.getCombinedSurface(h, n, 12)
        
        return self.insetSurface(c)

    def createStaticBlits(self, blitList) :
        Scoreboard.createStaticBlits(self, blitList)
        blitList.append( self.layout.getLeftSideCenteredBlit( self.fontSmallText.render("HITS", Colors.TEXT)[0] , CricketLayout.HITS_TITLE_HEIGHT) )
        blitList.append( self.layout.getRightSideCenteredBlit( self.fontSmallText.render("HITS", Colors.TEXT)[0] , CricketLayout.HITS_TITLE_HEIGHT) )
       # blitList.append( self.layout.getLeftSideCenteredBlit( self.fontSmallText.render("ERRORS", Colors.TEXT)[0] , CricketLayout.ERRORS_TITLE_HEIGHT) )
       # blitList.append( self.layout.getRightSideCenteredBlit( self.fontSmallText.render("ERRORS", Colors.TEXT)[0] , CricketLayout.ERRORS_TITLE_HEIGHT) )
        blitList.append( self.layout.getCenteredBlit( self.fontText.render("INNING", Colors.TEXT)[0] , CricketLayout.INNING_TITLE_HEIGHT) )
        blitList.append( self.layout.getCenteredBlit( self.fontText.render("WICKETS", Colors.TEXT)[0] , CricketLayout.OUTS_TITLE_HEIGHT) )
       
    def createDynamicBlits(self, blitList) :
        Scoreboard.createDynamicBlits(self, blitList)
        blitList.append( self.layout.getLeftSideCenteredBlit(self.insetSurface(self.hitsSurface.getValueAsSurface(self.state.getHits(GameState.HOME_INDEX) )), CricketLayout.HITS_VALUE_HEIGHT ) )
        blitList.append( self.layout.getRightSideCenteredBlit(self.insetSurface(self.hitsSurface.getValueAsSurface(self.state.getHits(GameState.GUEST_INDEX) )), CricketLayout.HITS_VALUE_HEIGHT ) )
   #     blitList.append( self.layout.getLeftSideCenteredBlit(self.insetSurface(self.errorsSurface.getValueAsSurface(self.state.getErrors(GameState.HOME_INDEX)) ), CricketLayout.ERRORS_VALUE_HEIGHT ) )
   #     blitList.append( self.layout.getRightSideCenteredBlit(self.insetSurface(self.errorsSurface.getValueAsSurface(self.state.getErrors(GameState.GUEST_INDEX)) ), CricketLayout.ERRORS_VALUE_HEIGHT ) )
        blitList.append( self.layout.getCenteredBlit(self.insetSurface(self.outSurface.getValueAsSurface(self.state.getOuts())), CricketLayout.OUTS_VALUE_HEIGHT ) )

        blitList.append(self.layout.getCenteredBlit(self.createInningSurface(), CricketLayout.INNING_BOTTOM_HALF_HEIGHT))


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



