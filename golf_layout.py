from layout import  Layout

class GolfLayout(Layout) :
    
    LEADER_COLS = [580, 640, 696, 756]
    FRAME_COLS = [20, 20, 20, 290, 290, 290]
    FRAME_ROWS = [6, 164, 321, 6, 164, 321]

    def __init__(self, window) :
        Layout.__init__(self, window)

