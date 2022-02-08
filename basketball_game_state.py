from scoreState import TimedGameState
from team_state import BasketballTeamState

class BasketballGameState(TimedGameState) :
    
    def __init__(self):
        #invoking the __init__ of the parent class 
        TimedGameState.__init__(self) 
        self.maxScore = 199
        self.teams = [BasketballTeamState(0, self.getMaxScore()), BasketballTeamState(0, self.getMaxScore())]
        self.TIME_INTERVAL = 12
        self.MINUTES_PER_PERIOD = 12
        self.MAX_SECONDS = self.MINUTES_PER_PERIOD * 60
        self.seconds = self.MAX_SECONDS

    def processSportSpecificKeys(self, event) :
        x=0

    def getTimeoutsTaken(self, team) :
        return self.teams[team].getTimeoutsTaken()

    def getTeamFouls(self, team) :
        return self.teams[team].getTeamFouls()