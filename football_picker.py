from scoreboard_picker import ScoreboardOption
import pygame
from colors import Colors

class FootballPicker() :
    USA_DINGBAT = "x"
    CANADA_DINGBAT = "y"

    def __init__(self, window) :
         self.choices = [ 
                        ScoreboardOption( self.fontImage, FootballPicker.USA_DINGBAT, self.fontText, "USA", FootballScoreboard(self.window)),
                        ScoreboardOption( self.fontImage, FootballPicker.CANADA_DINGBAT, self.fontText, "Canada", FootballScoreboard(self.window)),
                      ]

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
        
        for option in self.scoreboards :
           
            option.draw(self.window, ( 150 + (count % 3) * 240 , 20 + 154 * (count // 3)))
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
                    self.scoreboardIndex = (self.scoreboardIndex + 1) % (len(self.scoreboards) ) 
                    self.choices[self.scoreboardIndex].isSelected(True)    
                elif event.key == pygame.K_a:
                    self.choices[self.scoreboardIndex].isSelected(False)
                    self.scoreboardIndex = (self.scoreboardIndex - 1) % (len(self.scoreboards) ) 
                    self.choices[self.scoreboardIndex].isSelected(True)    
                elif event.key == pygame.K_s:
                    if (event.mod & pygame.KMOD_LSHIFT) :
                        self.running = False
                        break
                    else :
                        self.choices[self.scoreboardIndex].processSelection()




