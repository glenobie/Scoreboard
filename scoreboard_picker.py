import os
import socket
import pygame
import pygame.freetype
from hockey_scoreboard import HockeyScoreboard
from basketball_scoreboard import BasketballScoreboard
from football_scoreboard import FootballScoreboard
from baseball_scoreboard import BaseballScoreboard

os.environ['SDL_VIDEO_CENTERED'] = '1'

class ScoreboardOption :

    DEFAULT_COLOR = (255,255,255)
    HIGHLIGHT_COLOR = (255,0,0)

    DINGBAT_FILE = "sports.otf"
    TEXT_FILE    = "title-sb.ttf"
    DINGBAT_SIZE = 120
    TEXT_SIZE = 40

    SPACING = 10 # between icon and title

    def __init__(self, dingbat, text, scoreboard) :
        self.fontImages = pygame.freetype.Font(ScoreboardOption.DINGBAT_FILE, ScoreboardOption.DINGBAT_SIZE)
        self.fontText = pygame.freetype.Font(ScoreboardOption.TEXT_FILE, ScoreboardOption.TEXT_SIZE)

        self.dingbat = dingbat
        self.text = text
        self.icon = self.fontImages.render(dingbat, ScoreboardOption.DEFAULT_COLOR)[0]
        
        self.title = self.fontText.render(text, ScoreboardOption.DEFAULT_COLOR)[0]
        self.scoreboard = scoreboard
        
    def processSelection(self) :
        self.scoreboard.run()

    def draw(self, window, position) :
        iconX = titleX = position[0]
        iconY = position[1]
        titleY = position[1] + ScoreboardOption.SPACING + self.icon.get_size()[1] 

        # compare widths in order to set x position
        if self.icon.get_size()[0] > self.title.get_size()[0]  : 
            titleX = iconX + (self.icon.get_size()[0] - self.title.get_size()[0]) / 2 
        else :
            iconX = titleX + (self.title.get_size()[0] - self.icon.get_size()[0]) / 2 

        window.blit(self.icon, (iconX, iconY) )
        window.blit(self.title, (titleX, titleY) )

    def isSelected(self, selected) :
        if selected :
            self.icon = self.fontImages.render(self.dingbat, ScoreboardOption.HIGHLIGHT_COLOR)[0]
            self.title = self.fontText.render(self.text, ScoreboardOption.HIGHLIGHT_COLOR)[0]
        else :
            self.icon = self.fontImages.render(self.dingbat, ScoreboardOption.DEFAULT_COLOR)[0]
            self.title = self.fontText.render(self.text, ScoreboardOption.DEFAULT_COLOR)[0]

    
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

    def __init__(self):
            pygame.init()
            self.flags = 0
            if socket.gethostname() == "scoreboard":
                self.flags = pygame.FULLSCREEN
            self.window = pygame.display.set_mode((800,480), self.flags)
            
            pygame.display.set_caption("SCOREBOARD")

            
            self.scoreboards = [ ScoreboardOption( ScoreboardPicker.HOCKEY_DINGBAT, "Hockey", HockeyScoreboard(self.window)),
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
        self.window.fill((0,0,0))
        x = 44
        for option in self.scoreboards :
            option.draw(self.window, (x,140) )
            x += option.get_width() + 60

        pygame.display.update()   

    def run(self):
            self.running = True
            while self.running:
                self.processInput()
                self.update()
                self.render()

picker = ScoreboardPicker()
picker.run()

pygame.quit()