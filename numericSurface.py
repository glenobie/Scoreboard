import pygame.freetype
import pygame

class NumericSurface () :

    # Lays out a number on a surface

    def __init__(self, font, color, value=0, digitsToDisplay=3, displayLeadingZeroes=False, spacing=8): 
        
        self.font = font
        self.color = color
        self.displayLeadingZeroes = displayLeadingZeroes
        self.digitsToDisplay = digitsToDisplay
        self.spacing = spacing
        self.maxDigitWidth = self.font.get_metrics("0")[0][1] - self.font.get_metrics("0")[0][0]
        self.maxDigitHeight = self.font.get_metrics("0")[0][3] - self.font.get_metrics("0")[0][2]
        self.setValue(value)

    def setValue(self, value)  :
         self.value = value
         self.leadingZeroes = self.digitsToDisplay - len(str(self.value))
         
        
    def getValueAsSurface(self, value) :
        self.setValue(value)
        surface = pygame.Surface( self.getSurfaceSize())

        x = 0
        for i in range(0, self.leadingZeroes) :
            if (self.displayLeadingZeroes) :
                surface.blit( self.font.render("0", self.color)[0], (x, 0)) 
#            else :
#                surface.blit(self.font.render(" ", self.color)[0], (x, 0))
            x += self.spacing + self.maxDigitWidth

        for digit in str(self.value) :
            x += self.maxDigitWidth - (self.font.get_metrics(digit)[0][1] - self.font.get_metrics(digit)[0][0])
            surface.blit(self.font.render(digit, self.color)[0], (x, 0)  )
            x += self.spacing + (self.font.get_metrics(digit)[0][1] - self.font.get_metrics(digit)[0][0])
            
        
        return surface

    def getSurfaceSize(self) :
        width = self.digitsToDisplay * self.maxDigitWidth + ( (self.digitsToDisplay - 1) * self.spacing) 
        height = self.maxDigitHeight
        return ( width, height)


        


   
