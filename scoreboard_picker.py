import os
import socket
import pygame
import pygame.freetype
from football_game_state import FootballGameState
from hockey_scoreboard import HockeyScoreboard
from basketball_scoreboard import BasketballScoreboard
from football_scoreboard import FootballScoreboard
from baseball_scoreboard import BaseballScoreboard
from boxing_scoreboard import BoxingScoreboard
from cricket_scoreboard import CricketScoreboard
from tennis_scoreboard import TennisScoreboard
from bowling_scoreboard import BowlingScoreboard
from golf_scoreboard import GolfScoreboard
from colors import Colors
from fonts import Fonts

os.environ['SDL_VIDEO_CENTERED'] = '1'

class ScoreboardOption :

    SPACING = 10 # between icon and title

    def __init__(self, dingbatFont, dingbatChar, textFont, text, scoreboard) :

        self.dingbat = dingbatChar
        self.dingbatFont = dingbatFont
        self.fontText = textFont
        self.text = text
        self.icon = self.dingbatFont.render(self.dingbat, Colors.DEFAULT_COLOR)[0]
        self.iconWidth = self.icon.get_width()
        
        self.title = self.fontText.render(text, Colors.DEFAULT_COLOR)[0]
        self.titleWidth = self.title.get_width()
        self.scoreboard = scoreboard
        
    def processSelection(self) :
        self.scoreboard.run()

    def draw(self, window, position) : # position is center of object5
        iconX =  position[0] - (self.iconWidth / 2)
        titleX = position[0] - (self.titleWidth / 2)
        iconY = position[1]
        titleY = iconY + self.icon.get_height() + ScoreboardOption.SPACING
        window.blit(self.icon, (iconX, iconY) )
        window.blit(self.title, (titleX, titleY) )

    def isSelected(self, selected) :
        if selected :
            self.icon = self.dingbatFont.render(self.dingbat, Colors.HIGHLIGHT_COLOR)[0]
            self.title = self.fontText.render(self.text, Colors.HIGHLIGHT_COLOR)[0]
        else :
            self.icon = self.dingbatFont.render(self.dingbat, Colors.DEFAULT_COLOR)[0]
            self.title = self.fontText.render(self.text, Colors.DEFAULT_COLOR)[0]

    def get_width(self) :
        if self.icon.get_width() > self.title.get_width() :
            return self.icon.get_width()
        else : 
            return self.title.get_width()

#################################################

class FootballPicker() :
    USA_DINGBAT = "d"
    CANADA_DINGBAT = "K"

    def __init__(self, window) :
        self.window = window
        self.scoreboardIndex = 0
        self.fontImage1 = pygame.freetype.Font(Fonts.USA_FILE, Fonts.DINGBAT_SIZE)
        self.fontImage2 = pygame.freetype.Font(Fonts.CANADA_FILE, Fonts.DINGBAT_SIZE)
        self.fontText = pygame.freetype.Font(Fonts.TEXT_FILE, Fonts.SMALLEST_TEXT_SIZE)

        self.choices = [ 
                        ScoreboardOption( self.fontImage1, FootballPicker.USA_DINGBAT, self.fontText, "USA", FootballScoreboard(self.window)),
                        ScoreboardOption( self.fontImage2, FootballPicker.CANADA_DINGBAT, self.fontText, "Canada", FootballScoreboard(self.window, FootballGameState(3, 110))),
                      ]
        self.choices[self.scoreboardIndex].isSelected(True)

    def processSelection(self) :
        self.run()

    def run(self):
        self.running = True
        while self.running:
            self.processInput()
            self.render()

    def render(self) :
        self.window.fill(Colors.BACKGROUND)
        count = 0
        
        for option in self.choices :
           
            option.draw(self.window, ( 300 + count * 200 , 160))
            count += 1            

        pygame.display.update()   

    def processInput(self) :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_d:
                    self.choices[self.scoreboardIndex].isSelected(False)
                    self.scoreboardIndex = (self.scoreboardIndex + 1) % (len(self.choices) ) 
                    self.choices[self.scoreboardIndex].isSelected(True)    
                elif event.key == pygame.K_a:
                    self.choices[self.scoreboardIndex].isSelected(False)
                    self.scoreboardIndex = (self.scoreboardIndex - 1) % (len(self.choices) ) 
                    self.choices[self.scoreboardIndex].isSelected(True)    
                elif event.key == pygame.K_s:
                    if (event.mod & pygame.KMOD_LSHIFT) :
                        self.running = False
                        break
                    else :
                        self.choices[self.scoreboardIndex].processSelection()





##########################################################
class ScoreboardPicker :

    HOCKEY_DINGBAT = "l"
    BASKETBALL_DINGBAT = "P"
    BASEBALL_DINGBAT = "e"
    FOOTBALL_DINGBAT = "y"
    CRICKET_DINGBAT = "2"
    BOXING_DINGBAT = "L"
    TENNIS_DINGBAT = "v" # or "t" or "o" or "7" or "v"
    BOWLING_DINGBAT = "A"
    GOLF_DINGBAT = "B"

    def __init__(self):
            pygame.init()
            pygame.mouse.set_visible(False)
            self.flags = 0
            if socket.gethostname() == "raspberrypi":
                self.flags = pygame.FULLSCREEN
            self.window = pygame.display.set_mode((800,480), self.flags)
            
            pygame.display.set_caption("SCOREBOARD")
            self.fontImage1 = pygame.freetype.Font(Fonts.DINGBAT_FILE, Fonts.DINGBAT_SIZE)
            self.fontImage2 = pygame.freetype.Font(Fonts.DINGBAT2_FILE, Fonts.DINGBAT_SIZE)
            self.fontText = pygame.freetype.Font(Fonts.TEXT_FILE, Fonts.SMALLEST_TEXT_SIZE)

            
            self.scoreboards = [ 
                                 ScoreboardOption( self.fontImage1, ScoreboardPicker.BASEBALL_DINGBAT, self.fontText,  "Baseball", BaseballScoreboard(self.window)),
                                 ScoreboardOption( self.fontImage1, ScoreboardPicker.FOOTBALL_DINGBAT, self.fontText, "Football", FootballPicker(self.window)),
                                 ScoreboardOption( self.fontImage1, ScoreboardPicker.BASKETBALL_DINGBAT, self.fontText, "Basketball", BasketballScoreboard(self.window)),
                                 ScoreboardOption( self.fontImage1, ScoreboardPicker.HOCKEY_DINGBAT, self.fontText, "Hockey", HockeyScoreboard(self.window)),
                                 ScoreboardOption( self.fontImage2, ScoreboardPicker.CRICKET_DINGBAT, self.fontText, "Cricket", CricketScoreboard(self.window)),
                                 ScoreboardOption( self.fontImage1, ScoreboardPicker.BOXING_DINGBAT, self.fontText,"Boxing", BoxingScoreboard(self.window)),
                                 ScoreboardOption( self.fontImage1, ScoreboardPicker.TENNIS_DINGBAT, self.fontText, "Tennis", TennisScoreboard(self.window)),
                                 ScoreboardOption( self.fontImage1, ScoreboardPicker.BOWLING_DINGBAT, self.fontText, "Bowling", BowlingScoreboard(self.window)),
                                 ScoreboardOption( self.fontImage1, ScoreboardPicker.GOLF_DINGBAT, self.fontText, "Golf", GolfScoreboard(self.window))
                               ]

            self.scoreboardIndex = 0
            self.scoreboards[self.scoreboardIndex].isSelected(True)
            
            
    def update(self) :
        x=1

    def processInput(self) :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_d:
                    self.scoreboards[self.scoreboardIndex].isSelected(False)
                    self.scoreboardIndex = (self.scoreboardIndex + 1) % (len(self.scoreboards) ) 
                    self.scoreboards[self.scoreboardIndex].isSelected(True)    
                elif event.key == pygame.K_a:
                    self.scoreboards[self.scoreboardIndex].isSelected(False)
                    self.scoreboardIndex = (self.scoreboardIndex - 1) % (len(self.scoreboards) ) 
                    self.scoreboards[self.scoreboardIndex].isSelected(True)    
                elif event.key == pygame.K_s:
                    if (event.mod & pygame.KMOD_LSHIFT) :
                        self.running = False
                        break
                    else :
                        self.scoreboards[self.scoreboardIndex].processSelection()
                    
    def render(self) :
        self.window.fill(Colors.BACKGROUND)
        count = 0
        
        for option in self.scoreboards :
           
            option.draw(self.window, ( 150 + (count % 3) * 240 , 20 + 154 * (count // 3)))
            count += 1            

            # x += option.get_width() + 60

        pygame.display.update()   

    def run(self):
            self.running = True
            while self.running:
                self.processInput()
                #self.update()
                self.render()

picker = ScoreboardPicker()
picker.run()

pygame.quit()

