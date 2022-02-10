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

########################
class TeamStateWithTimeouts(TeamState) :
    def __init__(self, score, maxScore, maxTimeouts) :
        TeamState.__init__(self, score, maxScore) 
        self.maxTimeouts = maxTimeouts
        self.timeoutsTaken = 0

    def modifyTimeoutsTaken(self, value) :
        self.timeoutsTaken += value
        if (self.timeoutsTaken > self.maxTimeouts) :
            self.timeoutsTaken = self.maxTimeouts
        elif (self.timeoutsTaken < 0) :
            self.timeoutsTaken = 0
  
    def getTimeoutsTaken(self):
        return self.timeoutsTaken

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
class BasketballTeamState(TeamStateWithTimeouts):
    def __init__(self, score, maxScore, maxTimeouts, maxTeamFouls) :
        TeamStateWithTimeouts.__init__(self, score, maxScore, maxTimeouts) 
        self.teamFouls = 0
        self.maxTeamFouls = maxTeamFouls

    def modifyTeamFouls(self, value) :
        self.teamFouls += value
        if self.teamFouls > self.maxTeamFouls :
            self.teamFouls = self.maxTeamFouls
        if self.teamFouls < 0 :
                self.teamFouls = 0

    def getTeamFouls(self):
        return self.teamFouls

 

#########################
class FootballTeamState(TeamStateWithTimeouts) :
    def __init__(self, score, maxScore, maxTimeouts) :
        TeamStateWithTimeouts.__init__(self, score, maxScore, maxTimeouts)
    

#########################
class BaseballTeamState(TeamState) :
    def __init__(self, score, maxScore) :
        TeamState.__init__(self, score, maxScore)
        self.hits = 0
        self.errors = 0

    def getErrors(self) :
        return self.errors

    def getHits(self) :
        return self.hits

    def modifyHits(self, value) :
        self.hits += value
        if self.hits < 0 :
            self.hits = 0
    
    def modifyErrors(self, value) :
        self.errors += value
        if self.errors < 0 :
            self.errors = 0
  
    