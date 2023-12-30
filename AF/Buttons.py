from Prog import background
import pygame
class Button:
    def __init__(self, x, y, width, height, text, value, screen, calx = 0, caly=0):
        self.text = background.SHOW_TEXT(x + calx, y + caly, text, screen, 50, (255, 255, 255))
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.value = value
        self.screen = screen
    def show(self):
        self.text.show()
    def click_check(self, pos):
        if self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height:
            return self.value
        return None

        
    