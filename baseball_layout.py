from layout import  Layout

class BaseballLayout(Layout) :  

    INNING_HEIGHT = 200
    OUTS_HEIGHT = 260
   
    HITS_TITLE_HEIGHT = 180
    ERRORS_TITLE_HEIGHT = 340

    HITS_VALUE_HEIGHT  = 240
    ERRORS_VALUE_HEIGHT  = 400



    def __init__(self, window) :
        Layout.__init__(self, window)

