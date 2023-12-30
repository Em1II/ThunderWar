import pygame, time, screeninfo
from Prog import background, techsounds

import random
pygame.init()
f = screeninfo.get_monitors()

cell_size = 20
cell_number = 20
map_lenth = 10000
width = f[0].width
height = f[0].height
screen = pygame.display.set_mode((width - 20, height - 50))
a1 = pygame.image.load('img/img;effects/ex.png')
a2 = pygame.image.load('img/img;effects/ex1.png')
a3 = pygame.image.load('img/img;effects/ex2.png')
a4 = pygame.image.load('img/img;effects/ex3.png')
a5 = pygame.image.load('img/img;effects/ex4.png')
GRAVITY = 0
trail_sprites = pygame.sprite.Group()
smoke_sprites = pygame.sprite.Group()
s1 = pygame.transform.scale(pygame.image.load('img/img;effects/ex.png'), (5, 5))
s2 = pygame.transform.scale(pygame.image.load('img/img;effects/ex1.png'), (5, 5))
s3 = pygame.transform.scale(pygame.image.load('img/img;effects/ex2.png'), (5, 5))
s4 = pygame.transform.scale(pygame.image.load('img/img;effects/ex3.png'), (5, 5))
s5 = pygame.transform.scale(pygame.image.load('img/img;effects/ex4.png'), (5, 5))
m1 = pygame.transform.scale(pygame.image.load('img/img;effects/ex.png'), (50, 50))
m2 = pygame.transform.scale(pygame.image.load('img/img;effects/ex1.png'), (50, 50))
m3 = pygame.transform.scale(pygame.image.load('img/img;effects/ex2.png'), (50, 50))
m4 = pygame.transform.scale(pygame.image.load('img/img;effects/ex3.png'), (50, 50))
m5 = pygame.transform.scale(pygame.image.load('img/img;effects/ex4.png'), (50, 50))
def huge_explosion(screen, x, y, ground=False):
    h = screeninfo.get_monitors()[0].height
    x = x - 100
    y = h - 300
    screen.blit(a1, (x, y))
    
    screen.blit(a2, (x, y))

    screen.blit(a3, (x, y))

    screen.blit(a4, (x, y))
    pygame.display.update()

    if ground:
        screen.blit(a5, (x - 400, y - 130))
    techsounds.play_bomb_or_dest()
def medium_explosion(screen, x, y):
    screen.blit(m1, (x, y))


    screen.blit(m2, (x, y))
    screen.blit(m3, (x, y))
    screen.blit(m4, (x, y))
    screen.blit(m5, (x, y))
    pygame.display.update()
    techsounds.play_bomb_or_dest()

def small_explosion(screen, x, y, ground=False):
    


    screen.blit(s1, (x, y))


    screen.blit(s2, (x, y))
    screen.blit(s3, (x, y))
    screen.blit(s4, (x, y))
    screen.blit(s5, (x, y))
    if ground:
        techsounds.play_30mm_hit_the_ground()
    else:
        techsounds.play_30mm_hit_the_target()


rocket_cloud = [pygame.image.load("img/img;effects/rocket_cloud2.png").convert_alpha()]
smoke_cloud = [pygame.image.load("img/img;effects/black_cloud.png").convert_alpha()]

class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера
    

    def __init__(self, pos, dx, dy, fire, group, kill_time):
        
        super().__init__(group)
        self.time = time.process_time()
        self.image = random.choice(fire)
        self.rect = self.image.get_rect()
        self.kill_time =  kill_time
        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = GRAVITY
        self.x = pos[0]

    def update(self, shift):
        # применяем гравитационный эффект: 
        # движение с ускорением под действием гравитации
        self.velocity[1] += 0
        # перемещаем частицу
        
        self.velocity[0] -= 0.001
        self.velocity[1] -= 0.001
        self.x += self.velocity[0]
        self.rect.x  = self.x - shift
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if time.process_time() - self.time > self.kill_time:
            self.kill()
        
        
def create_rocket_trail(position, shift):
    global trail_sprites
    # количество создаваемых частиц
    particle_count = 5
    
    # возможные скорости
    
    for _ in range(particle_count):
        Particle(position, random.randint(-20, 20)/100, random.randint(-20, 20)/100, rocket_cloud, trail_sprites, 3)
    trail_sprites.update(shift)
    trail_sprites.draw(screen)
def create_smoke(position, shift):
    global smoke_sprites
    position = (position[0] + shift + 10 + random.randint(0, 20), position[1] + 30)
    # количество создаваемых частиц
    particle_count = random.randint(-1, 2)
    
    # возможные скорости
    numbers = range(-100, -20)
    if particle_count > 0:
        for _ in range(particle_count):
            Particle(position, random.choice(numbers)/100, -2, smoke_cloud, smoke_sprites, random.randint(100, 250)/100)
    smoke_sprites.update(shift)
    smoke_sprites.draw(screen)
    
    
    
