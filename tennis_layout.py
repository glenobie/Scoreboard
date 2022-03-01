from layout import  Layout

class TennisLayout(Layout) :
    
    ROWS = [100,200]
    COLS = [10, 400, 470, 540, 610, 680] # [ dot/name/pts, set1, set2, set3, set4, set5]

    def __init__(self, window) :
        Layout.__init__(self, window)

