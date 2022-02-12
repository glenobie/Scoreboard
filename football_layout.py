from layout import LayoutWithClock, Layout

class FootballLayout(LayoutWithClock) :  

    TIMEOUTS_TITLE_HEIGHT = 180

    TIMEOUTS_VALUE_HEIGHT  = 240

    DOWN_HEIGHT = 260
    YTG_HEIGHT = 330
    DISTANCE_HEIGHT = 410
    BALL_TEXT_HEIGHT = 200
    BALL_VALUE_HEIGHT = 260



    def __init__(self, window) :
        LayoutWithClock.__init__(self, window)

