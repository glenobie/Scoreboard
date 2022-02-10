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