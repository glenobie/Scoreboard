from layout import LayoutWithClock, Layout

class FootballLayout(LayoutWithClock) :  

    TIMEOUTS_TITLE_HEIGHT = 180

    TIMEOUTS_VALUE_HEIGHT  = 240


    def __init__(self, window) :
        LayoutWithClock.__init__(self, window)

