from scoreState import GameState, TimedGameState
from team_state import FootballTeamState

class FootballGameState(TimedGameState) :

    DOWN_STRINGS = ("1ST", "2ND", "3RD", "4TH")
    NUM_DOWNS = 4
    
    def __init__(self):
        #invoking the __init__ of the parent class 
        TimedGameState.__init__(self) 
        self.teams = [FootballTeamState(0, self.getMaxScore(), 3), 
                       FootballTeamState(0, self.getMaxScore(), 3)]

        self.TIME_INTERVAL = 15
        self.MINUTES_PER_PERIOD = 15
        self.MAX_SECONDS = self.MINUTES_PER_PERIOD * 60
        self.seconds = self.MAX_SECONDS

        self.lineOfScrimmage = 0 # 0 to 99
        self.down = 1
        self.yardsToGain = 10

        self.teamPossessingBall = GameState.HOME_INDEX

    def getDownAsString(self) :
        return FootballGameState.DOWN_STRINGS[self.down-1]

    def getDown(self) :
        return self.down

    def getYardsToGain(self) :
        return self.yardsToGain

    def modifyDown(self) :
        self.down += 1
        if (self.down > FootballGameState.NUM_DOWNS) :
            self.down = 1
        
    def getPossessingTeam(self) :
        return self.teamPossessingBall

    def changePossessingTeam(self) :
        self.teamPossessingBall = (self.teamPossessingBall + 1) % 2

    def getLineOfScrimmage(self) :
        return self.lineOfScrimmage

    def modifyLineOfScrimmage(self, value, doDecrement = False) :
        if (doDecrement) :
            self.lineOfScrimmage -= value
            self.yardsToGain += value
            if self.lineOfScrimmage < 0 :
                self.lineOfScrimmage = 0
            if self.yardsToGain > 99 :
                self.yardsToGain = 99
        else :
            self.lineOfScrimmage += value
            self.yardsToGain -= value
            if self.lineOfScrimmage > 99 :
                self.lineOfScrimmage = 99
            if self.yardsToGain < 0 :
                self.yardsToGain = 0

    def resetDownAndDistance(self) :
        self.yardsToGain = 10
        self.down = 1