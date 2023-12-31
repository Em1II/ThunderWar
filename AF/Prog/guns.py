import pygame
import screeninfo
import random
import time
from Prog import rot, animations, techsounds
import math
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, xpl, ypl, angel, munition, calx, caly, group, radius=0, damage=1):
        super().__init__(group)
        self.angel = angel
        self.xpl = xpl
        self.ypl = ypl
        self.radius = radius
        self.damage = damage
        self.munition = rot.rott(self.angel, munition)
        self.rect = self.munition.get_rect()
        self.mask = pygame.mask.from_surface(self.munition)
        self.image = self.munition
        self.caly = caly
        self.calx = calx
        self.x = x + self.calx
        self.y = y + self.caly

        self.rect.centery = y + caly
        self.rect.centerx = x + calx
    def update(self, shift):
        
        self.rect.centerx = self.x + self.xpl - shift
        self.rect.centery += self.ypl
        self.x += self.xpl
           
class Bomb(Bullet):
    def __init__(self, x, y, angel, munition, xpl, ypl, calx, caly, group, radius, damage):
        super().__init__(x, y + 10, xpl, ypl, angel, munition, calx, caly, group, radius, damage)
        self.y = 0
        
       
        
    def update(self, shift):
        self.y += self.ypl
        self.rect.centery -= self.ypl
        self.rect.centerx = self.x + math.sqrt(-self.y * self.xpl) - shift
        
        
class Rocket(Bullet):
    def __init__(self, x, y, angel, munition, xpl, ypl, calx, caly, group, radius, damage):
        super().__init__(x, y, xpl, ypl, angel, munition, calx, caly, group, radius, damage)
        self.y = 0
        self.start_at = time.process_time()
    def update(self, shift):
        
        self.rect.centerx = self.x + self.xpl - shift
        self.rect.centery += self.ypl
        self.x += self.xpl
        animations.create_rocket_trail((self.x, self.rect.centery -10), shift)
        if time.process_time() - self.start_at > 10:
            self.kill()


class WEAPON:
    def __init__(self, sound_func, munition, rounds, rad, dam):
        self.sprite_group = pygame.sprite.Group()
        self.radius = rad
        self.damage = dam
        self.sound_func = sound_func
        self.munition = munition
        self.rounds = rounds
        self.boom = []
    def surface_collision(self, surface_group, screen):
        if self.sprite_group.sprites():
            munition_type = self.sprite_group.sprites()[0]
            for e in pygame.sprite.groupcollide(self.sprite_group, surface_group, dokilla=True, dokillb=False):
                x = e.rect.x
                y = e.rect.y
                self.animation(screen, x, y)
                self.boom.append([screen, x, y, munition_type])
        
        
    def draw_munition(self, screen, shift):
        self.sprite_group.update(shift)
        self.sprite_group.draw(screen)
    def splash(self, vehs):
            for boom in self.boom:
                for veh in vehs:
                
                    if abs(boom[1] - veh.coords.x) <= boom[3].radius:
                        veh.HP -= boom[3].damage
            self.boom.clear()
class ROCKET_LAUNCHER(WEAPON):
    def __init__(self, rounds, rad, dam):
        munition = pygame.image.load("img/img;effects/bomb5.png").convert_alpha()
        sound_func = techsounds.play_rocket_launch
        super().__init__(sound_func, munition, rounds, rad, dam)
        self.animation = animations.medium_explosion

    def launch(self, x, y, angel, xpl, ypl, calibrationx, calibrationy):
        if self.rounds > 0:
            self.rounds -= 1
            self.sound_func()
            Rocket(x, y, angel, self.munition, xpl, ypl, calibrationx, calibrationy, self.sprite_group, self.radius, self.damage)
    


class BOMB_BAY(WEAPON):

    def __init__(self, rounds, rad, dam):
        munition = pygame.image.load("img/img;effects/bomb5.png").convert_alpha()
        sound_func = techsounds.play_bomb_launch
        super().__init__(sound_func, munition, rounds, rad, dam)
        self.animation = animations.huge_explosion

        
    def launch(self, x, y, angel, xpl, ypl, calibrationx, calibrationy):
        if self.rounds > 0:
            self.rounds -= 1
            self.sound_func()
            Bomb(x, y, angel, self.munition, xpl, ypl, calibrationx, calibrationy, self.sprite_group, self.radius, self.damage)
    




class GUN:
    def __init__(self, burst, bullet, rounds, how_long, ch, ch1):
        self.sprite_group = pygame.sprite.Group()
        self.rounds = rounds
        self.burst = burst
        self.chanell = ch
        self.tracer = bullet
        self.chanell_mis = ch1
        self.mis = pygame.mixer.Sound('sounds/misfire.wav')
        self.pr = 0
        self.l = how_long
    def stop_firing(self):
        pygame.mixer.Channel(self.chanell).pause()
    def play_fire(self, curr):
        if curr - self.pr > self.l or self.pr == 0:
            pygame.mixer.Channel(self.chanell).play(self.burst)
            self.pr = curr
    def play_misfire(self):
        pygame.mixer.Channel(self.chanell_mis).play(self.mis)
    
    def add_fire(self, x, y, angel, curr, xpl, ypl, calibrationx, calibrationy):

        if self.rounds != 0:
            pygame.mixer.Channel(self.chanell).unpause()
            
            Bullet(x, y, xpl, ypl, angel, self.tracer, calibrationx, calibrationy, self.sprite_group)
            self.rounds -= 1
            self.play_fire(curr)
        else:
            self.stop_firing()
            self.play_misfire() #doesn't work
    def update(self, shift):
        self.sprite_group.update(shift)
    def surface_collision(self, surface_group, screen):
        for e in pygame.sprite.groupcollide(self.sprite_group, surface_group, dokilla=False, dokillb=False):
            x = e.rect.x
            y = e.rect.y
            animations.small_explosion(screen, x, y)
        
    def draw_tracers(self, screen, shift):
        self.update(shift)
        self.sprite_group.draw(screen)
        