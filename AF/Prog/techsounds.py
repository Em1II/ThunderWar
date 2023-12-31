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
def play_tractor():
    a = pygame.mixer.Sound('sounds/tractor.wav')
    pygame.mixer.Channel(905).play(a)
def play_engine():
    a = pygame.mixer.Sound('sounds/engine.flac')
    pygame.mixer.Channel(906).play(a)
def play_1():
    a = pygame.mixer.Sound('sounds/pole1.mp3')
    pygame.mixer.Channel(900).play(a)
def play_2():
    a = pygame.mixer.Sound('sounds/les3.mp3')
    pygame.mixer.Channel(901).play(a)
def play_3():
    a = pygame.mixer.Sound('sounds/les2.mp3')
    pygame.mixer.Channel(902).play(a)
def play_4():
    a = pygame.mixer.Sound('sounds/pole1.mp3')
    pygame.mixer.Channel(903).play(a)
def play_5():
    a = pygame.mixer.Sound('sounds/les.mp3')
    pygame.mixer.Channel(904).play(a)
def pause_all():
    pygame.mixer.Channel(904).pause()
    pygame.mixer.Channel(901).pause()
    pygame.mixer.Channel(902).pause()
    pygame.mixer.Channel(903).pause()
    pygame.mixer.Channel(905).pause()
    pygame.mixer.Channel(906).pause()

