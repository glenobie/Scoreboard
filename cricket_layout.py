from layout import  Layout

class CricketLayout(Layout) :
    
    TOTAL_TITLE_HEIGHT = 20
    TOTAL_VALUE_HEIGHT = 80


    WICKETS_TITLE_HEIGHT = 180
    WICKETS_VALUE_HEIGHT = 230

    OVERS_TITLE_HEIGHT = 320
    OVERS_VALUE_HEIGHT = 370
   
    BATTER_NUMBER_HEIGHT = 20
    BATTER_RUNS_HEIGHT = 80

    LAST_TITLE_HEIGHT = 210
    LAST_VALUE_HEIGHT = 260


    def __init__(self, window) :
        Layout.__init__(self, window)

