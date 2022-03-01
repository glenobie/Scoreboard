from layout import  Layout

class BowlingLayout(Layout) :
    
    ROW1 = 100
    ROW2 = 260

    FRAME_SPACING = 68
    LEFT_MARGIN = 10
    
    PINS_FONT_SIZE = 36
    SCORE_FONT_SIZE = 36

    def __init__(self, window) :
        Layout.__init__(self, window)

