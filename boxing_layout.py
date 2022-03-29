from layout import LayoutWithClock, Layout

class BoxingLayout(LayoutWithClock) :  

    ENDURANCE_TITLE_HEIGHT = 190
    TKO_TITLE_HEIGHT = 340

    ENDURANCE_VALUE_HEIGHT  = 240
    TKO_VALUE_HEIGHT  = 390


    def __init__(self, window) :
        LayoutWithClock.__init__(self, window)
