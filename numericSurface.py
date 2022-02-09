import pygame.freetype
import pygame

class NumericSurface () :

    # Lays out a number on a surface

    def __init__(self, font, color, maxValue=199, displayLeadingZeroes=False, spacing=8) :
        self.font = font
        self.color = color
        self.displayLeadingZeroes = displayLeadingZeroes
        self.maxValue = maxValue
        self.maxDigits = len(str(maxValue))

        maxDigitWidth = self.font.get_metrics("0")[0][1] - self.font.get_metrics("0")[0][0]
        oneDigitWidth = self.font.get_metrics("1")[0][1] - self.font.get_metrics("1")[0][0]

        self.height = self.font.get_metrics("0")[0][3] - self.font.get_metrics("0")[0][2]
        
        self.width = (self.maxDigits - 1) * spacing
        
        self.positions = [] # right edge of each of the digits
        nextPosition = 0
        if str(maxValue).startswith("1") :
            nextPosition += oneDigitWidth
        else :
            nextPosition += maxDigitWidth
        self.positions.append(nextPosition)
        
        for i in range(1, self.maxDigits) :
            nextPosition += spacing + maxDigitWidth
            self.positions.append(nextPosition)

        self.width = nextPosition

    def displayAllDigits(self, surface, value) :
        donePrintingLeadingZeroes = False
        i = 0
        for digit in value :
            digitWidth = self.font.get_metrics(digit)[0][1] - self.font.get_metrics(digit)[0][0]
            xPos = self.positions[i] - digitWidth         

            if digit.startswith("0") :
                if (self.displayLeadingZeroes or donePrintingLeadingZeroes or i == len(value)-1) :
                     surface.blit(self.font.render(digit, self.color)[0], (xPos, 0)  )
            else :
                donePrintingLeadingZeroes = True
                surface.blit(self.font.render(digit, self.color)[0], (xPos, 0)  )
            i += 1
 
    def getValueAsSurface(self, value) :
        surface = pygame.Surface((self.width, self.height))
       
        valueAsString = str(value)
        #fill string to maxDigits
        for i in range(0, self.maxDigits - len(valueAsString))    :
            valueAsString = "0" + valueAsString
          
        self.displayAllDigits(surface, valueAsString)    
                    
        return surface

    
     
        

        return combinedSurface

        


   
