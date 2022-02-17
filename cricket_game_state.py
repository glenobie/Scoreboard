
from scoreState import GameState

class CricketBatter() :

    def __init__(self, value) :
        self.runs = 0
        self.number = value

    def setNumber(self, value) :
        self.number = value

    def modifyRuns(self, value) :
        self.runs += value
        if (self.runs < 0 ): self.runs = 0

    def resetRuns(self) :
        self.runs = 0
        
    def getNumber(self) :
        return self.number

    def getRuns(self) :
        return self.runs

    

class CricketGameState(GameState) :
    
    MAX_WICKETS = 10
    MAX_BATTERS = 11

    def __init__(self):
        #invoking the __init__ of the parent class 
        GameState.__init__(self) 
        self.maxScore = 999
        self.lastInnings = 0
        self.total = 0
        self.lockedTotal = 0
        self.changeSides()
  
    def changeLeftBatter(self) :
        self.lockedTotal += self.leftBatter.getRuns()
        self.leftBatter.resetRuns()

    def getOvers(self) :
        return self.overs
    
    def getWickets(self) :
        return self.wickets

    def changeSides(self) :
        self.lastInnings = self.total
        self.total = 0
        self.wickets = 0
        self.lastWicket = 0
        self.overs = 0
        self.leftBatter = CricketBatter(1)
        self.rightBatter =  CricketBatter(2)

    def recordScore(self):
        self.lastWicket = self.total
        

    def modifyTime(self, doDecrement=False) :
        # add/subtract overs from team in field
        adj = 1
        if (doDecrement) : adj = -1
        self.overs += adj
        if self.overs < 0 : self.overs = 0

    def incrementWickets(self) :
        self.wickets = (self.wickets + 1) % CricketGameState.MAX_WICKETS

    def getTotal(self) :
        return self.total

    def getLeftBatterNumber(self) :
        return self.leftBatter.getNumber()

    def getRightBatterNumber(self) :
        return self.rightBatter.getNumber()
        
    def getLeftBatterRuns(self) :
        return self.leftBatter.getRuns()

    def getRightBatterRuns(self) :
        return self.rightBatter.getRuns()

    def modifyLeftBatterRuns(self, doDecrement=False) :
        adj = 1
        if doDecrement : adj = -1
        self.leftBatter.modifyRuns(adj)
        self.total = self.lockedTotal + self.leftBatter.getRuns() + self.rightBatter.getRuns()

    def modifyRightBatterRuns(self, doDecrement=False) :
        adj = 1
        if doDecrement : adj = -1
        self.rightBatter.modifyRuns(adj)
        self.total = self.lockedTotal + self.leftBatter.getRuns() + self.rightBatter.getRuns()

    def incrementLeftBatterNumber(self) :
        self.leftBatter.setNumber((self.leftBatter.getNumber()  % CricketGameState.MAX_BATTERS) + 1)

    def incrementRightBatterNumber(self) :
        self.rightBatter.setNumber((self.rightBatter.getNumber()  % CricketGameState.MAX_BATTERS) + 1)

    def getLastInnings(self) :
        return self.lastInnings

    def getLastWicket(self) :
        return self.lastWicket

    def changeRightBatter(self) :
        self.lockedTotal += self.rightBatter.getRuns()
        self.rightBatter.resetRuns()

    def changeLeftBatter(self) :
        self.lockedTotal += self.leftBatter.getRuns()
        self.leftBatter.resetRuns()
        
    def swapBatters(self) :
        temp = self.leftBatter
        self.leftBatter = self.rightBatter
        self.rightBatter = temp