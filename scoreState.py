import pygame
from team_state import TeamState


class GameState :

    HOME_INDEX = 0
    GUEST_INDEX = 1
    
    def __init__(self) : 
        self.teams = [TeamState(0), TeamState(0)]

    def modifyScore(self, index, doDecrement=False):
        if doDecrement :
            self.teams[index].decrementScore()
        else :
            self.teams[index].incrementScore()

    def modifyHomeScore(self, doDecrement=False) :
        self.modifyScore(GameState.HOME_INDEX, doDecrement)

    def modifyGuestScore(self, doDecrement=False) :
        self.modifyScore(GameState.GUEST_INDEX, doDecrement)

###########################   
class TimedGameState(GameState):
    def __init__(self) : 
        GameState.__init__(self)
        self.period = 1
        self.maxPeriods = 4  
        self.seconds = 0
        self.timeDivisionName = "Quarter"

    def getSeconds(self):
        return self.seconds

    def getHomeScore(self) :
            return self.teams[GameState.HOME_INDEX].getScore()

    def getGuestScore(self) :
            return self.teams[GameState.GUEST_INDEX].getScore()

    def getPeriod(self) :
        return self.period

    def modifyPeriod(self) :
        self.period = self.period % self.maxPeriods + 1

    def getTimeDivisionName(self) :
        return self.timeDivisionName

    def modifyTime(self, doIncrement=False):
        if doIncrement :
            self.seconds += self.TIME_INTERVAL
            if self.seconds > self.MAX_SECONDS :
                self.seconds = self.MAX_SECONDS
        else :
            self.seconds -= self.TIME_INTERVAL
            if self.seconds < 0 :
                self.seconds = 0


