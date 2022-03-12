from scoreState import GameState, TimedGameState
from team_state import FootballTeamState

class FootballGameState(TimedGameState) :

    DOWN_STRINGS = ("1ST", "2ND", "3RD", "4TH")

    GOAL_TO_GO = -1000
    
    def __init__(self, maxDowns=4, fieldSize=100):
        #invoking the __init__ of the parent class 
        TimedGameState.__init__(self) 
        self.teams = [FootballTeamState(0, self.getMaxScore(), 3), 
                       FootballTeamState(0, self.getMaxScore(), 3)]

        self.TIME_INTERVAL = 15
        self.MINUTES_PER_PERIOD = 15
        self.MAX_SECONDS = self.MINUTES_PER_PERIOD * 60
        self.seconds = self.MAX_SECONDS
        self.MaxDowns = maxDowns

        self.lineOfScrimmage = 20 # 1 to 99
        self.down = 1
        self.yardsToGain = 10
        self.fieldSize = fieldSize

        self.teamPossessingBall = GameState.HOME_INDEX

    def getDownAsString(self) :
        return FootballGameState.DOWN_STRINGS[self.down-1]

    def getDown(self) :
        return self.down

    def getYardsToGain(self) :
        return self.yardsToGain

    def modifyDown(self) :
        self.down += 1
        if (self.down > self.MaxDowns) :
            self.down = 1
        
    def getPossessingTeam(self) :
        return self.teamPossessingBall

    def changePossessingTeam(self) :
        self.teamPossessingBall = (self.teamPossessingBall + 1) % 2
        self.lineOfScrimmage = self.fieldSize - self.lineOfScrimmage

    # between 0 and 50
    def getLineOfScrimmage(self) :
        halfFieldYard = self.lineOfScrimmage
        if (halfFieldYard > self.fieldSize / 2) :
            halfFieldYard = self.fieldSize - halfFieldYard
        return halfFieldYard


    def modifyLineOfScrimmage(self, value, doDecrement = False) :
        if (doDecrement) :
            self.lineOfScrimmage -= value
            self.yardsToGain += value
            if self.lineOfScrimmage < 0 :
                self.lineOfScrimmage = 0
            if self.yardsToGain > self.fieldSize - 1 :
                self.yardsToGain = self.fieldSize -1
            elif self.yardsToGain < 0 :
                self.yardsToGain = FootballGameState.GOAL_TO_GO
        else :
            self.lineOfScrimmage += value
            self.yardsToGain -= value
            if self.lineOfScrimmage > self.fieldSize - 1 :
                self.lineOfScrimmage = self.fieldSize - 1
            if self.yardsToGain < 0 :
                self.yardsToGain = FootballGameState.GOAL_TO_GO

    def resetDownAndDistance(self) :
        self.yardsToGain = 10
        if self.fieldSize - self.lineOfScrimmage < 10 : 
            self.yardsToGain = FootballGameState.GOAL_TO_GO
        self.down = 1

    def getYardsToEndzone(self) :
        return self.fieldSize - self.lineOfScrimmage

    def getLineToGain(self) :
        line = self.lineOfScrimmage + self.yardsToGain
        if line > self.fieldSize / 2 :
            line = self.fieldSize - line
        if line < 0 :
            line = 0
        return line
