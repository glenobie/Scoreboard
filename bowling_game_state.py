
from scoreState import GameState

class Bowler() :

    PINS = ["-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "/", "X"]
    NUM_SCORES = 11
   
    def __init__(self, bowling) :
        self.frames = [(0,0), (0,0), (0,0)] # 0 to 11, 10=spare, 11=strike
        self.scoreByFrame = [0, 0, 0]
        self.bowling = bowling
 
    def changeBowler(self) :
        self.bowling = not(self.bowling)
    
class BowlingGameState(GameState) :
    
    MAX_FRAMES = 3

    def __init__(self):
        #invoking the __init__ of the parent class 
        GameState.__init__(self) 
 
        self.bowlers = [Bowler(True), Bowler(False)]

    def modifyTime(self, t=False) :
        for p in self.bowlers :
            p.changeBowler()
        
    def getPlayerFrames(self, playerIndex ):
        return self.bowlers[playerIndex].frames

               
    def modifyPins(self, playerIndex, frameIndex, ballIndex, doDecrement) :
        adj = 1
        if doDecrement : adj = -1
        p = self.bowlers[playerIndex].frames[frameIndex][ballIndex]
        self.bowlers[playerIndex].frames[frameIndex][ballIndex] = (p + adj) % (Bowler.NUM_SCORES + 1)
              
    def getPins(self, playerIndex, frameIndex, ballIndex) :
        return Bowler.PINS[ self.bowlers[playerIndex].frames[frameIndex][ballIndex] ]
    
    def computeScoresByFrame(self) :
        x=0