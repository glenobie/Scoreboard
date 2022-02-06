
from football_game_state import FootballGameState
from numericSurface import NumericSurface
from scoreboard import TimedScoreboard
from scoreboard import Colors
from scoreboard import Fonts

class FootballScoreboard(TimedScoreboard):
    def __init__(self, window):
        TimedScoreboard.__init__(self, window)
        self.state = FootballGameState()
        self.scoreText = NumericSurface(self.fontScore, Colors.SCORE, 0, 2)

    def createSportSpecificStaticParts(self, blitList) :
        x=0

    def createSportSpecificSDynamicParts(self, blitList) :
        TimedScoreboard.createSportSpecificSDynamicParts(self, blitList)

