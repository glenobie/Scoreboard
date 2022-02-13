from layout import LayoutWithClock, Layout

class BasketballLayout(LayoutWithClock) :  

    TEAM_FOULS_TITLE_HEIGHT = 190
    TIMEOUTS_TITLE_HEIGHT = 340

    TEAM_FOULS_VALUE_HEIGHT  = 240
    TIMEOUTS_VALUE_HEIGHT  = 390


    def __init__(self, window) :
        LayoutWithClock.__init__(self, window)
