from scoreState import TimedGameState
from team_state import FootballTeamState

class FootballGameState(TimedGameState) :
    
    def __init__(self):
        #invoking the __init__ of the parent class 
        TimedGameState.__init__(self) 
        self.teams = [FootballTeamState(0, self.getMaxScore()), FootballTeamState(0, self.getMaxScore())]

        
        self.TIME_INTERVAL = 15
        self.MINUTES_PER_PERIOD = 15
        self.MAX_SECONDS = self.MINUTES_PER_PERIOD * 60
        self.seconds = self.MAX_SECONDS

    def processSportSpecificKeys(self, event) :
        x=0