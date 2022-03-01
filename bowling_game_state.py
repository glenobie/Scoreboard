
from scoreState import GameState

class Frame() :
    EMPTY = 0
    SPARE = 11
    STRIKE = 12
    PINS = [" ", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "/", "X"]
    BALL_1_SCORES = 11
    NUM_SCORES = 13
    

    def __init__(self, value) :
        self.balls = [Frame.EMPTY, Frame.EMPTY, Frame.EMPTY] # index into PINS
        self.score = 0
        self.value = value # frame number 1 to 10
        self.isEmpty = True
    
    def isSpare(self) :
        return self.balls[1] == Frame.SPARE

    def isStrike(self) :
        return self.balls[1] == Frame.STRIKE
    
    def isEmpty( self ) :
        return self.balls[0] == Frame.EMPTY or self.balls[1] == Frame.EMPTY

    def getDisplay(self, index) :
        return Frame.PINS[self.balls[index]]

    def isTenth(self) :
        return self.value == 10

    def modifyPins(self, ballIndex, value) :
        if (ballIndex == 0) :
            self.balls[ballIndex] = ( self.balls[ballIndex] + 1 ) % Frame.BALL_1_SCORES
        else :
            self.balls[ballIndex] = ( self.balls[ballIndex] + 1 ) % Frame.NUM_SCORES
        self.computeScore()


             
class Bowler() :

    def __init__(self, bowling) :
        self.frames = []
        for i in range(BowlingGameState.MAX_FRAMES) :
            self.frames.append( Frame(i+1) )
        self.bowling = bowling
 
    def changeBowler(self) :
        self.bowling = not(self.bowling)

    def modifyPins(self, frameIndex, ballIndex, value) :
        self.frames[frameIndex].modifyPins(ballIndex, value)

    def computeScoresByFrame(self) :
        self.score = 234


    
class BowlingGameState(GameState) :

    MAX_FRAMES = 10

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
        p = self.bowlers[playerIndex].modifyPins(frameIndex, ballIndex, adj)
              
    def getPins(self, playerIndex, frameIndex, ballIndex) :
        return BowlingGameState.PINS[ self.bowlers[playerIndex].frames[frameIndex][ballIndex] ]
    
