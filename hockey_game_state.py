
from team_state import HockeyTeamState
from scoreState import TimedGameState
import pygame

class HockeyGameState(TimedGameState) :
    
    def __init__(self):
        #invoking the __init__ of the parent class 
        TimedGameState.__init__(self) 
        self.maxScore = 19
        
        self.teams = [ HockeyTeamState(0, self.getMaxScore()), HockeyTeamState(0, self.getMaxScore()) ]
        

        self.TIME_INTERVAL = 20
        self.MINUTES_PER_PERIOD = 20
        self.MAX_SECONDS = self.MINUTES_PER_PERIOD * 60
        
        self.seconds = self.MAX_SECONDS
        self.maxPeriods = 3
        self.timeDivisionName = "Period"
  
    def modifyTime(self, doIncrement=False) :
        TimedGameState.modifyTime(self, doIncrement)
        if doIncrement :
            self.incrementPenaltyClocks(self.TIME_INTERVAL)
        else:
            self.incrementPenaltyClocks(-self.TIME_INTERVAL)
            
    def getPenaltySeconds(self, team, index) :
        return self.teams[team].getPenaltyClock(index)

    def modifyPenaltyClock(self, team, index=0) :
        if (self.teams[team].getPenaltyClock(index) == 0) :
            self.teams[team].setPenaltyClock(index, 120)
        elif (self.teams[team].getPenaltyClock(index) == 120) :
            self.teams[team].setPenaltyClock(index, 300)
        else :
            self.teams[team].setPenaltyClock(index, 0)

    def incrementPenaltyClocks(self, interval) :
        for i in range(len(self.teams)) :
            self.teams[i].modifyAllPenaltyClocks(interval)


    
