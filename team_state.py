class TeamState :
    def __init__(self, score, maxScore) : 
        self.score = score
        self.maxScore = maxScore

    def getScore(self) :
        return self.score

    def decrementScore(self) :
        self.score -= 1
        if self.score < 0 :
            self.score = 0

    def incrementScore(self) :
        if (self.score < self.maxScore) :
            self.score += 1 

##################
class HockeyTeamState(TeamState):
    def __init__(self, score, maxScore) : 
        TeamState.__init__(self, score, maxScore)
        self.penaltyClocks = [ 0, 0 ] # two clocks, in seconds

    def setPenaltyClock(self, index, value) :
        self.penaltyClocks[index] = value

    def getPenaltyClock(self, index) :
        return self.penaltyClocks[index]

    def modifyAllPenaltyClocks(self, value) :
        for i in range(len(self.penaltyClocks)) :
            self.penaltyClocks[i] += value
            if self.penaltyClocks[i] <= 0 :
                self.penaltyClocks[i] = 0

###################
class BasketballTeamState(TeamState):
    def __init__(self, score, maxScore) :
        TeamState.__init__(self, score, maxScore) 
        self.timeoutsTaken = 0
        self.teamFouls = 0

    def modifyTeamFouls(self, value) :
        self.teamFouls += value
        if self.teamFouls < 0 :
                self.teamFouls = 0

    def modifyTimeoutsTaken(self, value) :
        self.timeoutsTaken += value
        if (self.timeoutsTaken < 0) :
            self.timeoutsTaken = 0

    def getTeamFouls(self):
        return self.teamFouls

    def getTimeoutsTaken(self) :
        return self.timeoutsTaken

#########################
class FootballTeamState(TeamState) :
    def __init__(self, score, maxScore) :
        TeamState.__init__(self, score, maxScore)
        self.haveBall = False
        self.timeoutsTaken = 0
        self.lineOfScrimmage = 0
        self.down = 1
        self.yardsToGain = 10


