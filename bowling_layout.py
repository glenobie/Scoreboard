from layout import  Layout

class BowlingLayout(Layout) :
    
    ROWS = [100,200]
    COLS = [10, 200, 260, 320, 380, 440] # [ dot/name, frame1, frame2, ...]

    def __init__(self, window) :
        Layout.__init__(self, window)

