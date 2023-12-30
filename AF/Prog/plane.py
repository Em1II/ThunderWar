import pygame
from pygame.math import Vector2
from Prog import rot, vis, techsounds, animations, guns
import time
import screeninfo


class PLANE:
    def __init__(self, screen, l, ground, plane, max_spd, maneuvrability, hp, rockets, bombs, bullets):
        self.map_lenth = l
        self.plane_sprites = pygame.sprite.Group()
    
        self.plane = plane
        self.plane_sprite = pygame.sprite.Sprite(self.plane_sprites)
        self.plane_sprite.rect = self.plane.get_rect()
        self.plane_sprite.mask = pygame.mask.from_surface(self.plane)
        self.plane_sprite.image = self.plane
        self.fire = guns.GUN(pygame.mixer.Sound('sounds/minigun.aiff'),  pygame.image.load('img/img;effects/tracer1.1.png'), bullets, 30, 1, 2)
        
        self.bomb_bay = guns.BOMB_BAY(bombs[0], bombs[1], bombs[2])
        self.rocket_launcher = guns.ROCKET_LAUNCHER(rockets[0], rockets[1], rockets[2])
        self.ground = ground
        self.plane_loc = Vector2(5, 10)
        self.speeds ={0: (90, 0), 1: (89, -1), 2: (88, -2), 3: (87, -3), 4: (86, -4), 5: (85, -5), 6: (84, -6), 7: (83, -7), 8: (82, -8), 9: (81, -9), 10: (80, -10), 11: (79, -11), 12: (78, -12), 13: (77, -13), 14: (76, -14), 15: (75, -15), 16: (74, -16), 17: (73, -17), 18: (72, -18), 19: (71, -19), 20: (70, -20), 21: (69, -21), 22: (68, -22), 23: (67, -23), 24: (66, -24), 25: (65, -25), 26: (64, -26), 27: (63, -27), 28: (62, -28), 29: (61, -29), 30: (60, -30), 31: (59, -31), 32: (58, -32), 33: (57, -33), 34: (56, -34), 35: (55, -35), 36: (54, -36), 37: (53, -37), 38: (52, -38), 39: (51, -39), 40: (50, -40), 41: (49, -41), 42: (48, -42), 43: (47, -43), 44: (46, -44), 45: (45, -45), 46: (44, -46), 47: (43, -47), 48: (42, -48), 49: (41, -49), 50: (40, -50), 51: (39, -51), 52: (38, -52), 53: (37, -53), 54: (36, -54), 55: (35, -55), 56: (34, -56), 57: (33, -57), 58: (32, -58), 59: (31, -59), 60: (30, -60), 61: (29, -61), 62: (28, -62), 63: (27, -63), 64: (26, -64), 65: (25, -65), 66: (24, -66), 67: (23, -67), 68: (22, -68), 69: (21, -69), 70: (20, -70), 71: (19, -71), 72: (18, -72), 73: (17, -73), 74: (16, -74), 75: (15, -75), 76: (14, -76), 77: (13, -77), 78: (12, -78), 79: (11, -79), 80: (10, -80), 81: (9, -81), 82: (8, -82), 83: (7, -83), 84: (6, -84), 85: (5, -85), 86: (4, -86), 87: (3, -87), 88: (2, -88), 89: (1, -89), 90: (0, -90), 91: (-1, -89), 92: (-2, -88), 93: (-3, -87), 94: (-4, -86), 95: (-5, -85), 96: (-6, -84), 97: (-7, -83), 98: (-8, -82), 99: (-9, -81), 100: (-10, -80), 101: (-11, -79), 102: (-12, -78), 103: (-13, -77), 104: (-14, -76), 105: (-15, -75), 106: (-16, -74), 107: (-17, -73), 108: (-18, -72), 109: (-19, -71), 110: (-20, -70), 111: (-21, -69), 112: (-22, -68), 113: (-23, -67), 114: (-24, -66), 115: (-25, -65), 116: (-26, -64), 117: (-27, -63), 118: (-28, -62), 119: (-29, -61), 120: (-30, -60), 121: (-31, -59), 122: (-32, -58), 123: (-33, -57), 124: (-34, -56), 125: (-35, -55), 126: (-36, -54), 127: (-37, -53), 128: (-38, -52), 129: (-39, -51), 130: (-40, -50), 131: (-41, -49), 132: (-42, -48), 133: (-43, -47), 134: (-44, -46), 135: (-45, -45), 136: (-46, -44), 137: (-47, -43), 138: (-48, -42), 139: (-49, -41), 140: (-50, -40), 141: (-51, -39), 142: (-52, -38), 143: (-53, -37), 144: (-54, -36), 145: (-55, -35), 146: (-56, -34), 147: (-57, -33), 148: (-58, -32), 149: (-59, -31), 150: (-60, -30), 151: (-61, -29), 152: (-62, -28), 153: (-63, -27), 154: (-64, -26), 155: (-65, -25), 156: (-66, -24), 157: (-67, -23), 158: (-68, -22), 159: (-69, -21), 160: (-70, -20), 161: (-71, -19), 162: (-72, -18), 163: (-73, -17), 164: (-74, -16), 165: (-75, -15), 166: (-76, -14), 167: (-77, -13), 168: (-78, -12), 169: (-79, -11), 170: (-80, -10), 171: (-81, -9), 172: (-82, -8), 173: (-83, -7), 174: (-84, -6), 175: (-85, -5), 176: (-86, -4), 177: (-87, -3), 178: (-88, -2), 179: (-89, -1), 180: (-90, -2), 181: (-89, 3), 182: (-88, 4), 183: (-87, 5), 184: (-86, 6), 185: (-85, 7), 186: (-84, 8), 187: (-83, 9), 188: (-82, 10), 189: (-81, 11), 190: (-80, 12), 191: (-79, 13), 192: (-78, 14), 193: (-77, 15), 194: (-76, 16), 195: (-75, 17), 196: (-74, 18), 197: (-73, 19), 198: (-72, 20), 199: (-71, 21), 200: (-70, 22), 201: (-69, 23), 202: (-68, 24), 203: (-67, 25), 204: (-66, 26), 205: (-65, 27), 206: (-64, 28), 207: (-63, 29), 208: (-62, 30), 209: (-61, 31), 210: (-60, 32), 211: (-59, 33), 212: (-58, 34), 213: (-57, 35), 214: (-56, 36), 215: (-55, 37), 216: (-54, 38), 217: (-53, 39), 218: (-52, 40), 219: (-51, 41), 220: (-50, 42), 221: (-49, 43), 222: (-48, 44), 223: (-47, 45), 224: (-46, 46), 225: (-45, 47), 226: (-44, 48), 227: (-43, 49), 228: (-42, 50), 229: (-41, 51), 230: (-40, 52), 231: (-39, 53), 232: (-38, 54), 233: (-37, 55), 234: (-36, 56), 235: (-35, 57), 236: (-34, 58), 237: (-33, 59), 238: (-32, 60), 239: (-31, 61), 240: (-30, 62), 241: (-29, 63), 242: (-28, 64), 243: (-27, 65), 244: (-26, 66), 245: (-25, 67), 246: (-24, 68), 247: (-23, 69), 248: (-22, 70), 249: (-21, 71), 250: (-20, 72), 251: (-19, 73), 252: (-18, 74), 253: (-17, 75), 254: (-16, 76), 255: (-15, 77), 256: (-14, 78), 257: (-13, 79), 258: (-12, 80), 259: (-11, 81), 260: (-10, 82), 261: (-9, 83), 262: (-8, 84), 263: (-7, 85), 264: (-6, 86), 265: (-5, 87), 266: (-4, 88), 267: (-3, 89), 268: (-2, 90), 269: (-1, 91), 270: (0, 90), 271: (1, 89), 272: (2, 88), 273: (3, 87), 274: (4, 86), 275: (5, 85), 276: (6, 84), 277: (7, 83), 278: (8, 82), 279: (9, 81), 280: (10, 80), 281: (11, 79), 282: (12, 78), 283: (13, 77), 284: (14, 76), 285: (15, 75), 286: (16, 74), 287: (17, 73), 288: (18, 72), 289: (19, 71), 290: (20, 70), 291: (21, 69), 292: (22, 68), 293: (23, 67), 294: (24, 66), 295: (25, 65), 296: (26, 64), 297: (27, 63), 298: (28, 62), 299: (29, 61), 300: (30, 60), 301: (31, 59), 302: (32, 58), 303: (33, 57), 304: (34, 56), 305: (35, 55), 306: (36, 54), 307: (37, 53), 308: (38, 52), 309: (39, 51), 310: (40, 50), 311: (41, 49), 312: (42, 48), 313: (43, 47), 314: (44, 46), 315: (45, 45), 316: (46, 44), 317: (47, 43), 318: (48, 42), 319: (49, 41), 320: (50, 40), 321: (51, 39), 322: (52, 38), 323: (53, 37), 324: (54, 36), 325: (55, 35), 326: (56, 34), 327: (57, 33), 328: (58, 32), 329: (59, 31), 330: (60, 30), 331: (61, 29), 332: (62, 28), 333: (63, 27), 334: (64, 26), 335: (65, 25), 336: (66, 24), 337: (67, 23), 338: (68, 22), 339: (69, 21), 340: (70, 20), 341: (71, 19), 342: (72, 18), 343: (73, 17), 344: (75, 16), 345: (77, 15), 346: (79, 14), 347: (81, 13), 348: (83, 12), 349: (85, 11), 350: (87, 10), 351: (89, 9), 352: (91, 8), 353: (93, 7), 354: (95, 6), 355: (94, 5), 356: (94, 4), 357: (93, 3), 358: (92, 2), 359: (91, 1)}
        self.vs = vis.VIS()
        self.HP = hp
        self.abs_loc = Vector2(5, 10)
        self.sc = screen
        self.engine = 50
        self.max_speed = max_spd
        self.acciliration = 0.01
        self.curr_speed = 25
        self.min_speed = 0
        self.min_eng = 30
        self.angel = 0
        self.maneuverability = maneuvrability
    def update(self):
        self.loc_update()
        self.angel %= 3600
        plane = rot.rott(self.angel, self.plane)
        self.plane_sprite.rect = plane.get_rect()
        self.plane_sprite.mask = pygame.mask.from_surface(plane)
        self.plane_sprite.rect.x = self.abs_loc.x
        self.plane_sprite.rect.y = self.abs_loc.y
        self.plane_sprite.image = plane
    def drop_bomb(self):

        self.bomb_bay.launch(self.plane_loc.x, self.plane_loc.y, self.angel, 5, -9, 0, 0)
    def launch_the_rockets(self):
        k = self.get_horllvert_speed()
        k1 = self.get_horllvert_speed()
        
        self.rocket_launcher.launch(self.plane_loc.x, self.plane_loc.y, self.angel, k[0] + k1[0], k[1] + k1[1], 15, 20)
    def open_fire(self):
        curr_time = time.perf_counter()
        k = self.get_horllvert_speed()
        k1 = self.get_horllvert_speed()
        
        self.fire.add_fire(self.plane_loc.x, self.plane_loc.y, self.angel, curr_time, k[0] + k1[0], k[1] + k1[1], 15, 20)
    def absolute_shift(self, w):
        mid = w // 2
        rmid = self.map_lenth - mid
        if self.plane_loc.x < mid:
            
            return 0
        if self.plane_loc.x >= rmid:

            return self.map_lenth - mid * 2
        
        
        return self.plane_loc.x - mid
    def getInfo(self):
        w, h = 50, 10
        x, y =  self.plane_loc.x, self.plane_loc.y
        return x, y, w, h

    def hurt(self, hurt):
        self.HP -= hurt
    
    
    #plane dir
   
    def update_curr_speed(self):
        self.curr_speed = max((self.max_speed - self.min_speed) / 100 * self.engine, self.min_speed)
    def get_info_for_aim(self, speed, angel):
        angel = (angel + 360) % 360
        perneunz_spd = speed / 90
        spds = self.speeds[angel]
        x_speed = perneunz_spd * spds[0]
        y_speed = perneunz_spd * spds[1]
        return (x_speed, y_speed)
    def get_horllvert_speed(self):
        self.update_curr_speed()
        angel = self.angel
        speed = self.curr_speed
        angel = (angel + 360) % 360
        perneunz_spd = speed / 90
        spds = self.speeds[angel]
        x_speed = perneunz_spd * spds[0]
        y_speed = perneunz_spd * spds[1]
        return (x_speed, y_speed)
    #plane dir
    #plane move
    def speed_up(self):
        self.engine += 1
        if self.engine >= 100:
            self.engine = 100
    def speed_low(self):
        self.engine -= 1
        if self.engine <= self.min_eng:
            self.engine = self.min_eng
        

    def go_up(self):
        self.angel += self.maneuverability
        if self.angel == 360:
            self.angel = 0
    def go_down(self):
        self.angel -= self.maneuverability
        if self.angel == -360:
            self.angel = 0
    def plane_draw(self):
        self.update()
        
        if self.vs.get_game_cond() != 'F':
            self.plane_sprites.draw(self.sc)
    #plane dir

    def plane_dest(self, x, y, ground=False):
        animations.huge_explosion(self.sc, x, y, True)
        self.vs.game_over()
    def fail_check(self):
        if self.HP <= 0:
            self.plane_dest(self.abs_loc.x, self.abs_loc.y)
            self.speed = 0

    def loc_update(self):
        self.fail_check()
        k = self.get_horllvert_speed()
        self.plane_loc.x += k[0]
        self.plane_loc.y += k[1]
        m = screeninfo.get_monitors()[0]
        if self.plane_loc.y < -50:
            self.angel *= -1
        if m.height < self.plane_loc.y + 130:
            x = self.abs_loc.x - 80
            y = self.abs_loc.y - 60
            self.plane_dest(x, y, ground = True)
        self.angel += 180

        if self.plane_loc.x < -100:
            self.angel += 180
        if self.plane_loc.x < self.map_lenth + 100:
            self.angel += 180

        if self.plane_loc.x > self.map_lenth - self.sc.get_width()//2:
            self.abs_loc.x = self.plane_loc.x + self.sc.get_width() - self.map_lenth
            
            
        if self.plane_loc.x < self.sc.get_width()//2:
            self.abs_loc.x = self.plane_loc.x
        self.abs_loc.y = self.plane_loc.y
    
        

    def get_engine(self):
        if self.engine > 30:
            return str(self.engine) + "%"
        return "Опасно малая тяга, управление тягой переданно инструктору"
    #plane move

