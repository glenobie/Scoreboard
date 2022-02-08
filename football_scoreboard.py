
from football_game_state import FootballGameState
from numericSurface import NumericSurface
from scoreboard import TimedScoreboard
from scoreboard import Colors
from scoreboard import Fonts

class FootballScoreboard(TimedScoreboard):
    def __init__(self, window):
        TimedScoreboard.__init__(self, window)
        self.state = FootballGameState()
        self.scoreText = NumericSurface(self.fontScore, Colors.SCORE, 99 )
        self.createStaticBlits(self.staticBlitList)

   
    def createStaticBlits(self, blitList) :
        TimedScoreboard.createStaticBlits(self, blitList)
       
    def createDynamicBlits(self, blitList) :
        TimedScoreboard.createDynamicBlits(self, blitList)

