import pygame
def rott(angle, img):
    try:return pygame.transform.rotate(img, angle)
    except:return pygame.transform.rotate(angle, img)