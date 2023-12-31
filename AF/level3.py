from Prog import background, plane, enemy, guns, vis, fill, techsounds, animations
from axil import load_image
import screeninfo
import sys
import time
import pygame
from random import randint
        

def run():
    f = screeninfo.get_monitors()

    pygame.init() #turn all of pygame on.

    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    env={"land": 'img/img;landscape/land1_yellow.jpg', "grass": 'img/img;landscape/grass200_yellow.png',
        "house": 'img/img;landscape/swamp_house200.png', "tree": 'img/img;landscape/spruce800.png'}
    cell_size = 20
    cell_number = 20
    map_lenth = 10000
    width = f[0].width
    height = f[0].height
    screen = pygame.display.set_mode((width - 20, height - 50))
    clock = pygame.time.Clock()

    SCREEN = pygame.USEREVENT
    pygame.time.set_timer(SCREEN, 100)
    

    fj = plane.PLANE(screen, map_lenth, "stub", pygame.image.load('img/img;tech/phantom_35.png').convert_alpha(), 50, 5, 250, [0, 0, 0], [70, 300, 400], 1000)
    pygame.mixer.set_num_channels(1000)
    
    vs = vis.VIS()
    def generate_vehs(dct):
        new = []
        for type in dct:
            for ch in range(dct[type]):
                if type == "AA":
                    new.append(enemy.AA_GUN(screen, fj.fire, fj, randint(1000, map_lenth), height, ch, 10000))
                elif type == "LT":
                    new.append(enemy.Light_Tank(screen, fj.fire, randint(0, map_lenth), height))
                elif type == "T":
                    new.append(enemy.Tank(screen, fj.fire, randint(0, map_lenth), height))
                elif type == "ART":
                    new.append(enemy.Art_sys(screen, fj.fire, randint(0, map_lenth), height))
        return new
    vehicles_dct = {"AA":0, "LT": 25, "T":40, "ART": 0}
    vehicles = generate_vehs(vehicles_dct)
    map1 = background.Map(map_lenth, width, vehicles, env, 3)



    fj.ground = map1.land.land_sprites


    FPS = 60
    clock = pygame.time.Clock()
    envs = time.process_time()
    engines = time.process_time()
    tractors = time.process_time()
    techsounds.play_3()
    techsounds.play_engine()
    techsounds.play_tractor()
    # 3; 4; 5; 6; 7; 8; 9; 10; 11 - channels for AA
    def recheck_sounds():
        nonlocal envs, engines, tractors
        f = time.process_time()
        if f - envs > 180:
            techsounds.play_3()
            envs = time.process_time()
        if f - engines > 4:
            techsounds.play_engine()
            engines = time.process_time()
        if f - tractors > 40:
            techsounds.play_tractor()
            tractors = time.process_time()

                
    while True:
        keys = pygame.key.get_pressed()  # checking pressed keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_b and (90 > (fj.angel)%360 or 270 < (fj.angel)%360 < 360):
                fj.drop_bomb()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
                fj.launch_the_rockets()
        
        
        q = 0
        for veh in vehicles:
            if veh.HP < 1:
                q += 1
        
        if vs.get_game_cond() == 'F' or q == len(vehicles):
            vs.game_not_over()
            return True if q == len(vehicles) else False
        
        if keys[pygame.K_s]:
            fj.go_down()
        if keys[pygame.K_w]:
            fj.go_up()
        if keys[pygame.K_d]:
            fj.speed_up()
        if keys[pygame.K_a]:
            fj.speed_low()
        if keys[pygame.K_SPACE]:
            fj.open_fire()
        if not keys[pygame.K_SPACE]:
            fj.fire.stop_firing()
        clock.tick(FPS)
        pygame.display.update()
        recheck_sounds()
        abs_shift = fj.absolute_shift(width)
        clock.tick(60)
        map1.sky.sky_draw(screen, 0, 0, abs_shift)
        background.SHOW_TEXT(10, 10, f'30мм: {str(fj.fire.rounds)}', screen, 20)
        background.SHOW_TEXT(10, 30, (f'Бомбы: {str(fj.bomb_bay.rounds)}' if (90 > (fj.angel)%360 or 270 < (fj.angel)%360 < 360) else "Сброс невозможен, опустите самолёт носом вниз"), screen, 20)
        background.SHOW_TEXT(10, 50, f'Ракеты: {str(fj.rocket_launcher.rounds)}', screen, 20)
        background.SHOW_TEXT(10, 70, f'Тяга: {fj.get_engine()}', screen, 20)
        background.SHOW_TEXT(10, 90, f'Прочность: {fj.HP}', screen, 20)
        background.SHOW_TEXT(10, 110, f'Осталось врагов: {len(vehicles) - q}', screen, 20)
        fj.fire.draw_tracers(screen, abs_shift)
        fj.bomb_bay.draw_munition(screen, abs_shift)
        
        fj.rocket_launcher.draw_munition(screen, abs_shift)
        
        fj.plane_draw()
        animations.create_rocket_trail((-1000, -1000), abs_shift, True)
        animations.create_smoke((-1000, -1000), abs_shift, True)
        map1.land.lands_draw(screen, abs_shift)
        fj.bomb_bay.splash(vehicles)
        fj.bomb_bay.surface_collision(map1.land.land_sprites, screen)
        fj.rocket_launcher.splash(vehicles)
        fj.rocket_launcher.surface_collision(map1.land.land_sprites, screen)
    
    

    

        clock.tick(FPS)
        pygame.display.update()
