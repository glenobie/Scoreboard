
from scoreState import GameState

class TennisPlayer() :

    def __init__(self) :
        self.points = 0
        self.sets = [0,0,0,0,0]
    

class TennisGameState(GameState) :
    
    def __init__(self):
        #invoking the __init__ of the parent class 
        GameState.__init__(self) 
 
        self.player1 = TennisPlayer()
        self.player2 =  TennisPlayer()

    def modifyTime(self) :
        # add/subtract overs from team in field
        adj = 1
        
    def getPlayer1Sets(self) :
        return self.player1.sets

    def getPlayer2Sets(self) :
        return self.player2.sets