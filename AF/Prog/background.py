import pygame, screeninfo
from random import randint

class SHOW_TEXT:
    def __init__(self, x, y, text, screen, font_size, color=(0, 0, 0)):
        self.font = pygame.font.Font(None, font_size)
        self.color = color
        self.text = text
        self.x = x
        self.y = y
        self.screen = screen
        self.show()

    def show(self):
        sur = self.font.render(self.text, False, self.color)
        self.screen.blit(sur, (self.x, self.y))
    def get_surface(self):
        return self.font.render(self.text, False, self.color)
class Cloud:
        def __init__(self, index, x, y):
            self.cloud = pygame.image.load(f'img/img;landscape/cloud{index}.png').convert_alpha()
            self.x = x
            self.y = y
class Map:
    def __init__(self, lenth, w, lands_fill, env, forest_index, sky_fill=True):
        self.land = LANDS(lands_fill, env, lenth//200, forest_index)
        self.sky = SKY(w, sky_fill, lenth)
        self.screen_width = w
        self.map_lenth = lenth
class LANDS:
    def __init__(self, fill=[], env={"land": 'img/img;landscape/land1_yellow.jpg', "grass": 'img/img;landscape/grass200_yellow.png',
                                     "house": 'img/img;landscape/swamp_house200.png', "tree": 'img/img;landscape/spruce800.png'}, lenth=20, forest_index=4):
        self.land = pygame.image.load(env["land"]).convert_alpha()
        self.grass = pygame.image.load(env["grass"]).convert_alpha()
        self.house = pygame.image.load(env["house"]).convert_alpha()
        self.tree = pygame.image.load(env["tree"]).convert_alpha()
        self.h = screeninfo.get_monitors()[0].height / 1.1
        self.filled = fill
        self.forest_index = forest_index
        self.lenth = lenth
        self.env_sprites = pygame.sprite.Group()
        self.land_sprites = pygame.sprite.Group()
        self.init()
        self.prev_shift = 0   
    def init_houses(self):
        houses = randint(0, int((self.lenth)/20))
        for e in range(houses):
            sprite_house = pygame.sprite.Sprite(self.env_sprites)
            sprite_house.rect = self.house.get_rect()
            sprite_house.image = self.house
            sprite_house.rect.x = (randint(0, self.lenth * 225))
            sprite_house.rect.y = self.h - 125
    def init_floor(self):
        for e in range(-1, self.lenth + 10):
            

            sprite = pygame.sprite.Sprite(self.land_sprites)
            sprite.rect = self.land.get_rect()
            sprite.image = self.land
            sprite.rect.x = e * 200
            
            sprite.rect.y = self.h + 20
            sprite.mask = pygame.mask.from_surface(self.land)

            sprite_grass = pygame.sprite.Sprite(self.env_sprites)
            sprite_grass.rect = self.grass.get_rect()
            sprite_grass.image = self.grass
            sprite_grass.rect.x = e * 200 + (randint(-100, 100))
            
            sprite_grass.rect.y = self.h - 100
    def init_faraway(self):
        #forest
        for e in range(6, self.lenth):
            if randint(0, self.forest_index) == self.forest_index:
                continue
            else:
                size = randint(300, 800)
                tree = pygame.transform.scale(self.tree, (int(432/(800/size)), size))
                sprite_tree = pygame.sprite.Sprite(self.env_sprites)

                sprite_tree.rect = tree.get_rect()
                sprite_tree.image = tree
                sprite_tree.rect.x = e * 200 + randint(0, 100)
                sprite_tree.rect.y = self.h - size + 30

                size = randint(300, 800)
                tree = pygame.transform.scale(self.tree, (int(432/(800/size)), size))
                sprite_tree = pygame.sprite.Sprite(self.env_sprites)

                sprite_tree.rect = tree.get_rect()
                sprite_tree.image = tree
                sprite_tree.rect.x = e * 200 + randint(50, 150)
                sprite_tree.rect.y = self.h - size + 30

                size = randint(300, 800)
                tree = pygame.transform.scale(self.tree, (int(432/(800/size)), size))
                sprite_tree = pygame.sprite.Sprite(self.env_sprites)

                sprite_tree.rect = tree.get_rect()
                sprite_tree.image = tree
                sprite_tree.rect.x = e * 200 - randint(0, 100)
                sprite_tree.rect.y = self.h - size + 30

                size = randint(300, 800)
                tree = pygame.transform.scale(self.tree, (int(432/(800/size)), size))
                sprite_tree = pygame.sprite.Sprite(self.env_sprites)

                sprite_tree.rect = tree.get_rect()
                sprite_tree.image = tree
                sprite_tree.rect.x = e * 200 + randint(0, 500)
                sprite_tree.rect.y = self.h - size + 30

                
    def init(self):
        self.init_houses()
        self.init_faraway()
        self.init_floor()
        
          
        
        
        
        
      
    def update(self, shift):
        
        for e in self.env_sprites.sprites():
            e.rect.x -= shift - self.prev_shift
        for e in self.land_sprites.sprites():
            e.rect.x -= shift - self.prev_shift
        self.prev_shift = shift
    def lands_draw(self, screen, shift):
        self.update(shift)
        
        
        self.land_sprites.draw(screen)
        
        for e in self.filled:
            e.draw(shift)
        self.env_sprites.draw(screen)


        

class SKY:
    
        

    def __init__(self, w, clouds, lenth):
        self.sky = pygame.image.load('img/img;landscape/sky.png').convert_alpha()
        if clouds is True:
            clouds = [Cloud(randint(1, 2), randint(0, lenth), randint(0, 300)) for e in range(randint(30, 60))]
        self.clouds = clouds
    def sky_draw(self, screen, x, y, shift):
        screen.blit(self.sky, (x, y))
        for cl in self.clouds:
            screen.blit(cl.cloud, (cl.x - shift, cl.y))