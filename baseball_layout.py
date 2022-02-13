from layout import  Layout

class BaseballLayout(Layout) :  

    INNING_TITLE_HEIGHT = 20
    INNING_TOP_HALF_HEIGHT = 50
    INNING_BOTTOM_HALF_HEIGHT = 80
    INNING_NUMBER_HEIGHT = 70

    OUTS_TITLE_HEIGHT = 240
    OUTS_VALUE_HEIGHT = 300
   
    HITS_TITLE_HEIGHT = 190
    ERRORS_TITLE_HEIGHT = 340

    HITS_VALUE_HEIGHT  = 240
    ERRORS_VALUE_HEIGHT  = 390 

    def __init__(self, window) :
        Layout.__init__(self, window)

