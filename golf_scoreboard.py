
from curses.ascii import SP
from re import S
from golf_game_state import GolfGameState, Golfer
from scoreboard import Scoreboard
from numericSurface import NumericSurface
from colors import Colors
from fonts import Fonts
from golf_layout import GolfLayout
import pygame

class GolfFrame() :
    def __init__(self, leftGolferID, rightGolferID, state, selected=False) :
        self.state = state
        self.leftGolferID = leftGolferID
        self.rightGolferID = rightGolferID
        self.selected = selected

    def setSelected(self, value) :
        self.selected = value

    def isSelected(self) :
        return self.selected

    def hasGolfer(self, g) :
        if self.leftGolferID == g.getID() or self.rightGolferID == g.getID() :
            return True
        return False

    def getHole(self) :
        return self.state.getGolfer(self.leftGolferID).getHoleAsString()

    def getLeftScore(self) :
        return self.state.getGolfer(self.leftGolferID).getScoreAsString()

    def getRightScore(self) :
        return self.state.getGolfer(self.rightGolferID).getScoreAsString()

    def getLeftID(self) :
        return str(self.leftGolferID)

    def getRightID(self) :
        return str(self.rightGolferID)


class GolfScoreboard(Scoreboard):

    def __init__(self, window):
        Scoreboard.__init__(self, window)


        self.fontLeaderboard = pygame.freetype.Font(Fonts.TEXT_FILE, Fonts.LEADERBOARD_SIZE)
        self.state = GolfGameState()
        self.frames = [GolfFrame(1,2, self.state, True), GolfFrame(3,4, self.state), GolfFrame(5, 6, self.state), 
                       GolfFrame(7,8, self.state), GolfFrame(9,10, self.state), GolfFrame(11,12, self.state)]

    
        self.leaderboardSurface = NumericSurface(self.fontLeaderboard, Colors.TEXT, 9)

        self.holeSurface = NumericSurface(self.fontVerySmallNumber, Colors.SCORE, 18)
        self.scoreSurface = NumericSurface(self.fontVerySmallNumber, Colors.SCORE, 999)
       

        self.layout = GolfLayout(window)
        self.selectedFrame = 0       

        self.createStaticBlits(self.staticBlitList)


    def getSurfaceForFrame(self, f) :
        s = pygame.Surface((220,150)) 
        s.fill(Colors.BACKGROUND)

        textColor = Colors.TEXT
        borderColor = Colors.DEFAULT_COLOR
        if f.isSelected() : 
            textColor = Colors.PERIOD
            borderColor = Colors.HIGHLIGHT_COLOR
        leftScore = self.insetSurface(self.scoreSurface.getValueAsSurface(f.getLeftScore()))
        rightScore = self.insetSurface(self.scoreSurface.getValueAsSurface(f.getRightScore()))
        pygame.draw.rect(s, borderColor, (0,0,220,150), 1)

        s.blit(leftScore, (4,32))
        s.blit(rightScore, (114,32))

        leftID = self.fontLeaderboard.render(f.getLeftID(), textColor)[0]
        rightID = self.fontLeaderboard.render(f.getRightID(), textColor)[0]

        x = (leftScore.get_width() - leftID.get_width() ) / 2
        s.blit(leftID, (4+x, 6))
        x = (rightScore.get_width() - rightID.get_width() ) / 2
        s.blit(rightID, (114+x, 6))

        t = self.fontSmallText.render("ON HOLE:", borderColor)[0]
        u = self.insetSurface(self.holeSurface.getValueAsSurface(f.getHole()))
        s.blit(self.getCombinedSurface(t, u, 4), (12,90) )

        return s



    def createStaticBlits(self, blitList) :
        y = 8
        s = self.fontLeaderboard.render("#", Colors.TEXT)[0]
        blitList.append( (s, (GolfLayout.LEADER_COLS[0]-s.get_width(), y )))
        s = self.fontLeaderboard.render("Par" , Colors.TEXT)[0]
        blitList.append( (s, (GolfLayout.LEADER_COLS[1]-s.get_width(), y)))
        s = self.fontLeaderboard.render("Thru" , Colors.TEXT)[0]
        blitList.append( (s, (GolfLayout.LEADER_COLS[2]-38, y)))
        s = self.fontLeaderboard.render("Back" , Colors.TEXT)[0]
        blitList.append( (s, (GolfLayout.LEADER_COLS[3]-28, y)))
       

    def createDynamicBlits(self, blitList) :
        golfers = self.state.getLeaderboard()
        color = Colors.TEXT
        index = 0
        startY = 40
        SPACING = Fonts.LEADERBOARD_SIZE = 32 + 4
        for g in golfers :  
            if self.frames[self.selectedFrame].hasGolfer(g) :
                color = Colors.PERIOD
            else :
                color = Colors.TEXT
            y = index * SPACING + startY
            s = self.fontLeaderboard.render(str(g.getID()) , color)[0]
            blitList.append( (s, (GolfLayout.LEADER_COLS[0]-s.get_width(), y )))
            s = self.fontLeaderboard.render(g.getScoreAsString() , color)[0]
            blitList.append( (s, (GolfLayout.LEADER_COLS[1]-s.get_width(), y)))
            s = self.fontLeaderboard.render(str(g.getCompletedHoleAsString()) , color)[0]
            blitList.append( (s, (GolfLayout.LEADER_COLS[2]-s.get_width(), y)))
            s = self.fontLeaderboard.render(str(g.getShotsBack()) , color)[0]
            blitList.append( (s, (GolfLayout.LEADER_COLS[3]-s.get_width(), y)))

            index += 1

        index = 0
        
        for f in self.frames : 
            x = GolfLayout.FRAME_COLS[index]
            y = GolfLayout.FRAME_ROWS[index]
            blitList.append( (self.getSurfaceForFrame(f), (x, y)))
            index += 1

 
    def cycleSelectedHole(self, adj) :
        self.frames[self.selectedFrame].setSelected(False)
        self.selectedFrame = (self.selectedFrame + adj) % len(self.frames)
        self.frames[self.selectedFrame].setSelected(True)
    
    def modifyLeftGolferScore(self, adj) :
        golferID = self.frames[self.selectedFrame].leftGolferID
        self.state.modifyScore(golferID, adj)

    def modifyRightGolferScore(self, adj) :
        golferID = self.frames[self.selectedFrame].rightGolferID
        self.state.modifyScore(golferID, adj)

    def processKeyPress(self, event) :
        if event.key == pygame.K_q:
            self.cycleSelectedHole(-1)
        elif event.key == pygame.K_e:
            self.cycleSelectedHole(1)
        elif event.key == pygame.K_a:
             self.modifyLeftGolferScore(1)
        elif event.key == pygame.K_d:
            self.modifyRightGolferScore(1)
        elif event.key == pygame.K_z:
            self.modifyLeftGolferScore(-1)
        elif event.key == pygame.K_c:
            self.modifyRightGolferScore(-1)
        elif event.key == pygame.K_x:
            self.state.incrementHoles()



