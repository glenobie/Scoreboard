
from basketball_game_state import BasketballGameState
from numericSurface import NumericSurface
from scoreboard import TimedScoreboard
from scoreboard import Colors
from scoreboard import Fonts

class BasketballScoreboard(TimedScoreboard):
    def __init__(self, window):
        TimedScoreboard.__init__(self, window)
        self.state = BasketballGameState()
        self.scoreText = NumericSurface(self.fontScore, Colors.SCORE, 0, 3)

    def createSportSpecificStaticParts(self, blitList) :
        x=0

    def createSportSpecificSDynamicParts(self, blitList) :
        TimedScoreboard.createSportSpecificSDynamicParts(self, blitList)

