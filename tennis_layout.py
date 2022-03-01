from layout import  Layout

class TennisLayout(Layout) :
    
    ROWS = [100,200]
    COLS = [10, 40, 380, 460, 540, 620, 700] # [ dot, name/ game score, set1, set2, set3, set4, set5]

    def __init__(self, window) :
        Layout.__init__(self, window)

