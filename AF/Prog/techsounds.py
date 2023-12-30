import pygame
pygame.mixer.init()
def play_rocket_launch():
    a = pygame.mixer.Sound('sounds/missel_launch.mp3')
    pygame.mixer.find_channel(True).play(a)
def play_bomb_launch():
    a = pygame.mixer.Sound('sounds/bomb_drop.mp3')
    pygame.mixer.find_channel(True).play(a)
def play_30mm_hit_the_ground():
    a = pygame.mixer.Sound('sounds/30mmExplosion.wav')
    pygame.mixer.find_channel(True).play(a)
def play_30mm_hit_the_target():
    a = pygame.mixer.Sound('sounds/30mmExplosion2.wav')
    pygame.mixer.find_channel(True).play(a)
def play_bomb_or_dest():
    a = pygame.mixer.Sound('sounds/explosion.wav')
    pygame.mixer.Channel(998).play(a)
