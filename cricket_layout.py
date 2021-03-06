from layout import  Layout

class CricketLayout(Layout) :
    
    TOTAL_TITLE_HEIGHT = 20
    TOTAL_VALUE_HEIGHT = 80


    WICKETS_TITLE_HEIGHT = 200
    WICKETS_VALUE_HEIGHT = 250

    OVERS_TITLE_HEIGHT = 320
    OVERS_VALUE_HEIGHT = 370
   
    BATTER_NUMBER_HEIGHT = 20
    BATTER_RUNS_HEIGHT = 80

    BATTING_TEAM_ROW2_TITLE_HEIGHT = 180
    BATTING_TEAM_ROW2_VALUE_HEIGHT = 230

    BOWLING_TEAM_ROW_TITLE_HEIGHT = 340
    BOWLING_TEAM_ROW_VALUE_HEIGHT = 390


    def __init__(self, window) :
        Layout.__init__(self, window)

