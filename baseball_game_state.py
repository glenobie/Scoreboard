
from re import S
from scoreState import GameState
from team_state import BaseballTeamState

class BaseballGameState(GameState) :
    
    def __init__(self):
        #invoking the __init__ of the parent class 
        GameState.__init__(self) 
        self.maxScore = 99
        self.teams = [BaseballTeamState(0, self.getMaxScore() ), 
                      BaseballTeamState(0, self.getMaxScore() )]
        self.inning = 1
        self.outs = 0
        self.teamAtBat = GameState.GUEST_INDEX

    def getHits(self, team) :
        return self.teams[team].getHits()
    
    def getErrors(self, team) :
        return self.teams[team].getErrors()

    def changeSides(self) :
        self.teamAtBat = (self.teamAtBat + 1) % 2
        if self.teamAtBat == GameState.GUEST_INDEX :
                self.inning += 1

    def undoSideChange(self) :
        if not(self.isGameStart()) :
            self.teamAtBat = (self.teamAtBat - 1) % 2
            if (self.teamAtBat == GameState.HOME_INDEX) :
                self.inning -= 1

    def modifyHits(self, team, doDecrement=False) :
        if doDecrement :
            self.teams[team].modifyHits(-1)
        else:
            self.teams[team].modifyHits(1)

    def modifyErrors(self, team, doDecrement=False) :
        if doDecrement :
            self.teams[team].modifyErrors(-1)
        else:
            self.teams[team].modifyErrors(1)

    def isGameStart(self) :
        return (self.inning == 1 and self.teamAtBat == GameState.GUEST_INDEX)
 
    def modifyTime(self, doDecrement=False) :
        if (doDecrement) :
            self.undoSideChange()
        else:
            self.changeSides()
            


    def modifyOuts(self) :
        self.outs = (self.outs+1) % 3

    def getOuts(self) :
        return self.outs
    
    def getInning(self) :
        return self.inning

    def getHalfInning(self) :
        if self.teamAtBat == GameState.GUEST_INDEX :
            s = "TOP"
        else :
            s = "BTM"
        return s

    def getTeamAtBat(self) :
        return self.teamAtBat
    