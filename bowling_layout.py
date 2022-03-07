from layout import  Layout

class BowlingLayout(Layout) :
    
    ROW1 = 100
    ROW2 = 290

    FRAME_SPACING = 68
    LEFT_MARGIN = 10

    FRAME_WIDTH = 66
    FRAME_HEIGHT =  86
    
    PINS_FONT_SIZE = 36
    SCORE_FONT_SIZE = 36

    def __init__(self, window) :
        Layout.__init__(self, window)

