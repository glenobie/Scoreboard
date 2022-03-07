from layout import  Layout

class TennisLayout(Layout) :
    
    ROWS = [140,240]
    COLS = [10, 400, 470, 540, 610, 680] # [ dot/name/pts, set1, set2, set3, set4, set5]
    SET_SPACING = 70

    def __init__(self, window) :
        Layout.__init__(self, window)

