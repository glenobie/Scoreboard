from scoreState import TimedGameState
from team_state import BoxerState

class BoxingGameState(TimedGameState) :
    
    def __init__(self):
        #invoking the __init__ of the parent class 
        TimedGameState.__init__(self) 
        self.maxScore = 99
        self.teams = [BoxerState(0, self.getMaxScore()), 
                      BoxerState(0, self.getMaxScore())]
        self.TIME_INTERVAL = 20
        self.MINUTES_PER_PERIOD = 3
        self.MAX_SECONDS = self.MINUTES_PER_PERIOD * 60
        self.seconds = self.MAX_SECONDS
        self.timeDivisionName = "Round"
        self.maxPeriods = 15

 

    def getEndurance(self, team) :
        return self.teams[team].getEndurance()
    


    def modifyEndurance(self, team, doIncrement=False) :
        if doIncrement :
            self.teams[team].modifyEndurance(1)
        else:
            self.teams[team].modifyEndurance(-1)