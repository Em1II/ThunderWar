import os

import pygame
def load_image(name, colorkey=None):
    try:
        image = pygame.image.load(name).convert_alpha()
    except pygame.error as message:
        print(message)
        raise SystemExit(message)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image