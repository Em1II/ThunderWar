import pygame
import math
import time
import random
from Prog import animations, techsounds, rot, guns, plane

from pygame.math import Vector2
AA_HEIGHT_CALIBRATION = 108
ARTILLELY_HEIGHT_CALIBRATION = 135
TANK_HEIGHT_CALIBRATION = 115
LIGHT_TANK_HEIGHT_CALIBRATION = 115
class EnemyVeh:
    def __init__(self, screen, img, imgDest, fire, x, y, hp, w, h):
        self.fireFJ = fire
        self.veh_undest = img
        self.veh_dest = imgDest
        self.cond = True
        self.HP = hp
        self.screen = screen
        self.coords = Vector2(x, y)
        self.origCoords = Vector2(x, y)
        self.w = w
        self.h = h
        self.x = self.coords.x
        self.y = self.coords.y
        self.x1 = self.x + self.w
        self.y1 = self.y + self.h

        self.veh_sprites = pygame.sprite.Group()
        self.veh_sprite = pygame.sprite.Sprite(self.veh_sprites)
        self.veh_sprite.rect = self.veh_undest.get_rect()
        self.veh_sprite.mask = pygame.mask.from_surface(self.veh_undest)
        self.veh_sprite.image = self.veh_undest
        self.veh_sprite.rect.x = x
        self.veh_sprite.rect.y = y
        self.smoke = 400
    def check_dest(self):
        if self.HP <= 0:
            self.cond = False
            animations.huge_explosion(self.screen, self.coords.x, self.coords.y, True)
    def do_dets(self):
        self.veh_sprite.image = self.veh_dest
    
    def check_colision(self, bullets, alive=True):
        
        collisions = pygame.sprite.groupcollide(bullets.sprite_group, self.veh_sprites, dokilla=True, dokillb=False)
        for e in collisions:
            x = e.rect.x
            y = e.rect.y
            animations.small_explosion(self.screen, x, y)
            self.HP -= 1
        if alive:
            self.check_dest()
    def update_pos(self, shift):
        self.coords.x = self.origCoords.x - shift
        self.veh_sprite.rect.x = self.coords.x
    def draw(self, shift):
        self.update_pos(shift)
        
        if self.cond is True:
            self.check_colision(self.fireFJ)
        else:
            self.do_dets()
            
            if self.smoke > 0:
                self.smoke -= 1
                animations.create_smoke(self.coords, shift)
        self.check_colision(self.fireFJ, False)
        self.veh_sprites.draw(self.screen)
class Tank(EnemyVeh):
    
    def __init__(self, screen, fire, x, y):
        self.undest = pygame.image.load('img/img;tech/tank38.png')
        self.dest = pygame.image.load('img/img;tech/tank38dest.png')

        super().__init__(screen, self.undest, self.dest, fire, x, y - TANK_HEIGHT_CALIBRATION, 500, 85, 38)
class Light_Tank(EnemyVeh):
    
    def __init__(self, screen, fire, x, y):
        self.undest = pygame.image.load('img/img;tech/light_tank42.png')
        self.dest = pygame.image.load('img/img;tech/light_tank42dest.png')
        super().__init__(screen, self.undest, self.dest, fire, x, y - LIGHT_TANK_HEIGHT_CALIBRATION, 250, 70, 42) 
class Art_sys(EnemyVeh):
    
    def __init__(self, screen, fire, x, y):
        self.undest = pygame.image.load('img/img;tech/artilelly.png')
        self.dest = pygame.image.load('img/img;tech/artilelly_dest.png')
        super().__init__(screen, self.undest, self.dest, fire, x, y - ARTILLELY_HEIGHT_CALIBRATION, 100, 100, 55)




class AA_GUN:
    def __init__(self, screen, fire, plane, x, y, chanel, rounds):
        y -= AA_HEIGHT_CALIBRATION
        self.shift=0
        self.fireFJ = fire
        self.plane = plane
        self.burst = 60
        self.track = pygame.image.load('img/img;tech/track.png').convert_alpha()
        self.tower = pygame.image.load('img/img;tech/tower.png').convert_alpha()
        self.burrel = pygame.image.load('img/img;tech/burrel.png').convert_alpha()
        self.firing = pygame.mixer.Sound('sounds/m249.wav')
        self.track_dest = pygame.image.load('img/img;tech/trackdest.png').convert_alpha()
        self.cond = True
        self.screen = screen
        self.angel = 130
        self.HP = 75
        self.chanel = chanel
        self.veh_sprites = pygame.sprite.Group()
        self.fire = guns.GUN(pygame.mixer.Sound('sounds/m249.wav'), pygame.image.load('img/img;effects/tracer1.1.png'), rounds, 1.5, self.chanel, 2)
        self.burrel_sprite = pygame.sprite.Sprite(self.veh_sprites)
        self.burrel_sprite.rect = self.burrel.get_rect()
        self.burrel_sprite.mask = pygame.mask.from_surface(self.burrel)
        self.burrel_sprite.image = self.burrel
        self.burrel_sprite.rect.x = x
        self.burrel_sprite.rect.y = y - 15
        
        self.track_sprite = pygame.sprite.Sprite(self.veh_sprites)
        self.track_sprite.rect = self.track.get_rect()
        self.track_sprite.mask = pygame.mask.from_surface(self.track)
        self.track_sprite.image = self.track
        self.track_sprite.rect.x = x
        self.track_sprite.rect.y = y

        

        self.tower_sprite = pygame.sprite.Sprite(self.veh_sprites)
        self.tower_sprite.rect = self.tower.get_rect()
        self.tower_sprite.mask = pygame.mask.from_surface(self.tower)
        self.tower_sprite.rect.x = x
        self.tower_sprite.rect.y = y - 10
        self.tower_sprite.image = self.tower

        


        self.coords = Vector2(x, y)
        self.origCoords = Vector2(x, y)
        self.w = 100
        self.h = 40
        self.x = self.coords.x
        self.y = self.coords.y - 15
        self.x1 = self.x + self.w
        self.y1 = self.y + self.h
        self.smoke = 400

        
    def check_hit(self, plane):
        hurt = 0
        hurt = len(pygame.sprite.groupcollide(self.fire.sprite_group, plane.plane_sprites, dokilla=True, dokillb=False))
        
        plane.hurt(hurt)
    def change_angel(self, k):
        self.angel += k
    
    def check_dest(self):
        if self.HP <= 0:
            self.cond = False
            animations.huge_explosion(self.screen, self.coords.x, self.coords.y, True)
    def showHitBox(self):
        
        pygame.draw.rect(self.screen, "red", (self.x, self.y, self.w, self.h), 1)
    def check_colision(self, bullets, alive=True):
        
        collisions = pygame.sprite.groupcollide(bullets.sprite_group, self.veh_sprites, dokilla=True, dokillb=False)
        for e in collisions:
            x = e.rect.x
            y = e.rect.y
            animations.small_explosion(self.screen, x, y, ground=False)
            self.HP -= 1
        if alive:
            self.check_dest()
    
    def firin(self):
        k = self.plane.get_info_for_aim(30, int(self.angel))
        self.update_burrel()
        if self.burst > 0:
            
            self.fire.add_fire(self.origCoords.x, self.origCoords.y, self.angel, time.process_time(), k[0], k[1], 75, -20)
        elif self.burst > -100:
            self.fire.stop_firing()
        else:
            self.burst = random.randint(50, 100)
        self.burst -= 1
    def ppause(self):
        pygame.mixer.Channel(self.chanel).pause()
    def update_burrel(self):
        
        self.burrel_sprite.image = rot.rott(self.angel, self.burrel)
        
    def take_aim(self, target):
            x = self.coords.x + 55
            y = self.coords.y - 20
            xt = target.x
            yt = target.y
            
            adj = abs(xt - x)
            ops = abs(yt - y)
            adj = adj if adj != 0 else adj + 1
            pr = self.angel
            self.angel = (math.degrees(math.atan(ops/adj)))
            if self.angel < 18:
                self.angel = 18
            if self.angel > 160:
                self.angel = 160
            if xt < x:
                self.angel += (90 - self.angel) * 2
            if self.angel > pr and self.angel - pr > 3:
                self.angel = pr + 3
            if self.angel <= pr and pr - self.angel > 3:
                self.angel = pr - 3
            if not(abs(x - xt) > 1500 or abs(y - yt) > 2000):  
                self.firin()
    def dest(self):
        self.track_sprite.image = self.track_dest
        self.ppause()
    def draw__(self):
        x = self.coords.x
        y = self.coords.y
        self.screen.blit(rot.rott(self.angel, self.burrel), (x + 55, y - 20))
        self.screen.blit(self.track, (x, y))

        self.screen.blit(self.tower, (x + 50, y - 10))
        self.screen.blit(self.tower, (x + 65, y - 9))
        self.screen.blit(rot.rott(135, self.tower), (x + 79, y - 7))

    def update_hitbox(self):
        self.x = self.coords.x
        self.y = self.coords.y - 15
        self.x1 = self.x + self.w
        self.y1 = self.y + self.h
    def update_pos(self, shift):
        self.coords.x = self.origCoords.x - shift
        self.tower_sprite.rect.x = self.origCoords.x - shift + 60
        self.burrel_sprite.rect.x = self.origCoords.x - shift + 60
        self.track_sprite.rect.x = self.origCoords.x - shift
        self.update_hitbox()
    def draw(self, shift):
        self.update_pos(shift)
        if self.cond is False:
            self.dest()
            if self.smoke > 0:
                self.smoke -= 1
                animations.create_smoke(self.coords, shift)
        else:

            self.check_hit(self.plane)
            self.take_aim(self.plane.abs_loc)
            self.fire.draw_tracers(self.plane.sc, shift)
            self.check_colision(self.fireFJ)
        self.check_colision(self.fireFJ, False)
        self.veh_sprites.draw(self.screen)
            

