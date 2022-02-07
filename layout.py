
class Layout :

    SPACING_HORIZONTAL      = 10
    HOME_GUEST_HEIGHT       = 20
    SCORE_HEIGHT            = 80

    def __init__(self, window) :
        self.window = window
        self.windowWidth = window.get_size()[0]
        self.windowThirds = (0, self.windowWidth / 3, self.windowWidth * 2 / 3)
        self.windowHeight = window.get_size()[1]   

    def getHorizontalCenter(self, surfaceObject) :
        return (self.windowWidth - surfaceObject.get_size()[0]) / 2
                
    def getLeftSideCenteredBlit(self, surface, height) :
        x = (self.windowThirds[1] - surface.get_size()[0] ) / 2
        return (surface, (x, height))

    def getRightSideCenteredBlit(self, surface, height) :
        x = self.windowThirds[2]
        space = self.windowWidth - x
        x += (space - surface.get_size()[0]) / 2
        return (surface, (x, height))

    def getCentererdBlit(self, surface, height) :
        x = self.getHorizontalCenter(surface)
        return (surface, (x, height))


class LayoutWithClock(Layout) :

    CLOCK_TIME_HEIGHT    = 20
    CLOCK_COLON_HEIGHT   = 40
    PERIOD_HEIGHT        = 200
    PERIOD_VALUE_HEIGHT  = 280


    def __init__(self, window) :
        Layout.__init__(self, window)
        self.minuteX = 0
        self.secondX = 0
        self.colonX = 0
        
    def getColonBlit(self, surface) :
        self.colonX = self.getHorizontalCenter(surface)
        self.colonWidth = surface.get_size()[0]
        return (surface , (self.colonX, LayoutWithClock.CLOCK_COLON_HEIGHT) )

    def getMinutesBlit(self, surface) :
        if (self.minuteX == 0) :
            self.minuteX = self.colonX - surface.get_size()[0] - Layout.SPACING_HORIZONTAL
        return (surface, (self.minuteX, LayoutWithClock.CLOCK_TIME_HEIGHT))
        
    def getSecondsBlit(self, surface) :
        if (self.secondX == 0) :
            self.secondX = self.colonX + self.colonWidth + Layout.SPACING_HORIZONTAL
            self.secondWidth = surface.get_size()[0]
        return (surface, (self.secondX, LayoutWithClock.CLOCK_TIME_HEIGHT))


class HockeyLayout(LayoutWithClock) :  

    PENALTY_1_HEIGHT = 180
    PENALTY_2_HEIGHT = 340

    PENALTY_1_COLON_HEIGHT = 260
    PENALTY_2_COLON_HEIGHT = 420

    PENALTY_1_TIME_HEIGHT  = 240
    PENALTY_2_TIME_HEIGHT  = 400


    def getLeftPenaltyColonBlit(self, colon, height) :
        blit = self.getLeftSideCenteredBlit(colon, height) 
        self.penaltyColonWidth = colon.get_size()[0]

        self.leftPenaltyColonX = blit[1][0] - (self.penaltyColonWidth * 2.5)

        return (colon, (self.leftPenaltyColonX, height))

    def getRightPenaltyColonBlit(self, colon, height) :
        blit = self.getRightSideCenteredBlit(colon, height) 
        self.penaltyColonWidth = colon.get_size()[0]

        self.rightPenaltyColonX = blit[1][0] - (self.penaltyColonWidth * 2.5)

        return (colon, (self.rightPenaltyColonX, height))

    def getLeftPenaltyMinutesBlit(self, surface, height) :
        x = self.leftPenaltyColonX - surface.get_size()[0] - Layout.SPACING_HORIZONTAL
        return (surface, (x, height))

    def getLeftPenaltySecondsBlit(self, surface, height) :
        x = self.leftPenaltyColonX + self.penaltyColonWidth + Layout.SPACING_HORIZONTAL
        return (surface, (x, height))

    def getRightPenaltyMinutesBlit(self, surface, height) :
        x = self.rightPenaltyColonX - surface.get_size()[0] - Layout.SPACING_HORIZONTAL
        return (surface, (x, height))

    def getRightPenaltySecondsBlit(self, surface, height) :
        x = self.rightPenaltyColonX + self.penaltyColonWidth + Layout.SPACING_HORIZONTAL
        return (surface, (x, height))
