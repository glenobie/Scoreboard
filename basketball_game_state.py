from scoreState import TimedGameState
from team_state import BasketballTeamState

class BasketballGameState(TimedGameState) :
    
    def __init__(self):
        #invoking the __init__ of the parent class 
        TimedGameState.__init__(self) 
        self.maxScore = 199
        self.teams = [BasketballTeamState(0, self.getMaxScore(), 9, 10 ), 
                      BasketballTeamState(0, self.getMaxScore(), 9, 10)]
        self.TIME_INTERVAL = 12
        self.MINUTES_PER_PERIOD = 12
        self.MAX_SECONDS = self.MINUTES_PER_PERIOD * 60
        self.seconds = self.MAX_SECONDS

 

    def getTeamFouls(self, team) :
        return self.teams[team].getTeamFouls()
    


    def modifyTeamFouls(self, team, doDecrement=False) :
        if doDecrement :
            self.teams[team].modifyTeamFouls(-1)
        else:
            self.teams[team].modifyTeamFouls(1)