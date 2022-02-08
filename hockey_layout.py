from layout import LayoutWithClock, Layout

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
