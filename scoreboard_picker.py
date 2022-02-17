import os
import socket
import pygame
import pygame.freetype
from hockey_scoreboard import HockeyScoreboard
from basketball_scoreboard import BasketballScoreboard
from football_scoreboard import FootballScoreboard
from baseball_scoreboard import BaseballScoreboard
from boxing_scoreboard import BoxingScoreboard
from cricket_scoreboard import CricketScoreboard
from colors import Colors
from fonts import Fonts

os.environ['SDL_VIDEO_CENTERED'] = '1'

class ScoreboardOption :

    SPACING = 10 # between icon and title

    def __init__(self, dingbat, text, scoreboard) :

        #home = str(Path.home())
        
        self.fontImages = pygame.freetype.Font(Fonts.DINGBAT_FILE, Fonts.DINGBAT_SIZE)
        self.fontText = pygame.freetype.Font(Fonts.TEXT_FILE, Fonts.SMALLEST_TEXT_SIZE)

        self.dingbat = dingbat
        self.text = text
        self.icon = self.fontImages.render(dingbat, Colors.DEFAULT_COLOR)[0]
        self.iconWidth = self.icon.get_size()[0]
        
        self.title = self.fontText.render(text, Colors.DEFAULT_COLOR)[0]
        self.titleWidth = self.title.get_size()[0]
        self.scoreboard = scoreboard
        
    def processSelection(self) :
        self.scoreboard.run()

    def draw(self, window, position) : # position is center of object
        

        iconX =  position[0] - (self.iconWidth / 2)
        titleX = position[0] - (self.titleWidth / 2)
        iconY = position[1]
        titleY = position[1] + ScoreboardOption.SPACING + self.icon.get_size()[1] 

        # compare widths in order to set x position
        #if self.icon.get_size()[0] > self.title.get_size()[0]  : 
        ##    titleX = iconX + (self.icon.get_size()[0] - self.title.get_size()[0]) / 2 
        #else :
        #    iconX = titleX + (self.title.get_size()[0] - self.icon.get_size()[0]) / 2 

        window.blit(self.icon, (iconX, iconY) )
        window.blit(self.title, (titleX, titleY) )

    def isSelected(self, selected) :
        if selected :
            self.icon = self.fontImages.render(self.dingbat, Colors.HIGHLIGHT_COLOR)[0]
            self.title = self.fontText.render(self.text, Colors.HIGHLIGHT_COLOR)[0]
        else :
            self.icon = self.fontImages.render(self.dingbat, Colors.DEFAULT_COLOR)[0]
            self.title = self.fontText.render(self.text, Colors.DEFAULT_COLOR)[0]

    
    def get_width(self) :
        if self.icon.get_size()[0] > self.title.get_size()[0] :
            return self.icon.get_size()[0] 
        else : 
            return self.title.get_size()[0]


class ScoreboardPicker :

    HOCKEY_DINGBAT = "l"
    BASKETBALL_DINGBAT = "P"
    BASEBALL_DINGBAT = "e"
    FOOTBALL_DINGBAT = "y"
    CRICKET_DINGBAT = "M"
    BOXING_DINGBAT = "L"

    def __init__(self):
            pygame.init()
            pygame.mouse.set_visible(False)
            self.flags = 0
            if socket.gethostname() == "raspberrypi":
                self.flags = pygame.FULLSCREEN
            self.window = pygame.display.set_mode((800,480), self.flags)
            
            pygame.display.set_caption("SCOREBOARD")

            
            self.scoreboards = [ ScoreboardOption( ScoreboardPicker.CRICKET_DINGBAT, "Cricket", CricketScoreboard(self.window)),
                                 ScoreboardOption( ScoreboardPicker.BOXING_DINGBAT, "Boxing", BoxingScoreboard(self.window)),
                                 ScoreboardOption( ScoreboardPicker.HOCKEY_DINGBAT, "Hockey", HockeyScoreboard(self.window)),
                                 ScoreboardOption( ScoreboardPicker.BASEBALL_DINGBAT, "Baseball", BaseballScoreboard(self.window)),
                                 ScoreboardOption( ScoreboardPicker.FOOTBALL_DINGBAT, "Football", FootballScoreboard(self.window)),
                                 ScoreboardOption( ScoreboardPicker.BASKETBALL_DINGBAT, "Basketball", BasketballScoreboard(self.window))
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
           
            option.draw(self.window, ( 150 + (count % 3) * 240 , 70 + 200 * (count // 3)))
            count += 1            

            # x += option.get_width() + 60

        pygame.display.update()   

    def run(self):
            self.running = True
            while self.running:
                self.processInput()
                #self.update()a
                self.render()

picker = ScoreboardPicker()
picker.run()

pygame.quit()