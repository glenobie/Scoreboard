
from scoreState import GameState

class TennisPlayer() :

    POINTS = [" 0", "15", "30", "40", "AD"] #99 for AD
    NUM_POINTS = 5

    def __init__(self) :
        self.pointsIndex = 0
        self.sets = [0,0,0,0,0]
    

class TennisGameState(GameState) :
    
    MAX_GAMES = 7

    def __init__(self):
        #invoking the __init__ of the parent class 
        GameState.__init__(self) 
 
        self.players = [TennisPlayer(), TennisPlayer()]

    def modifyTime(self) :
        # change the serving player
        adj = 1
        
    def getPlayerSets(self, playerIndex ):
        return self.players[playerIndex].sets


    def modifyGames(self, playerIndex, setIndex, doDecrement) :
        adj = 1
        if doDecrement : adj = -1
        self.players[playerIndex].sets[setIndex] = (self.players[playerIndex].sets[setIndex] + adj) % (TennisGameState.MAX_GAMES + 1)
                
    def modifyPoints(self, playerIndex, doDecrement) :
        adj = 1
        if doDecrement : adj = -1
        self.players[playerIndex].pointsIndex = (self.players[playerIndex].pointsIndex + adj) % TennisPlayer.NUM_POINTS

    def getPoints(self, playerIndex) :
        return TennisPlayer.POINTS[self.players[playerIndex].pointsIndex]