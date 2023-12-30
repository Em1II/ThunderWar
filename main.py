import pygame, sys, time
import screeninfo
import level1, level2, level3, level4, level5
from Buttons import Button
from axil import load_image

pygame.init()
f = screeninfo.get_monitors()
cell_size = 20
cell_number = 20
map_lenth = 10000
width = f[0].width
height = f[0].height
screen = pygame.display.set_mode((width - 20, height - 50))

FPS = 60
midw = screen.get_rect().width//2.3
midh = screen.get_rect().height//3
input_active = True
font = pygame.font.SysFont(None, 50)
text = "Введите cвой ник"
buttons = {"Top":Button(midw, midh, 170, 45, "Рекорды", "top", screen, calx=5), 
           "rules":Button(midw, midh + 50, 170, 45, "Правила", "rules", screen, calx=5),
             "1":Button(midw - 40, midh + 100, 50, 45, "1", "1", screen, calx=10, caly=5),
               "2":Button(midw + 10 , midh + 100, 50, 45, "2", "2", screen, calx=10, caly=5),
                 "3":Button(midw + 60, midh+ 100, 50, 45, "3", "3", screen, calx=10, caly=5), 
                 "4":Button(midw + 110, midh+ 100, 50, 45, "4", "4", screen, calx=10, caly=5), 
                 "5":Button(midw + 160, midh+ 100, 50, 45, "5", "5", screen, calx=10, caly=5)}
pygame.display.set_caption("Thunder War")

clock = pygame.time.Clock()
def terminate():
    pygame.quit()
    sys.exit()
def get_page(intro_text):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = midh
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = midw
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE] is True:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)
def start_screen():
    
    global text, input_active
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    text =  text[:-1]
                else:
                    text += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for but in buttons:
                    if buttons[but].click_check(pos) is None:
                        continue
                    else:
                        value = buttons[but].value
                        do(value)
        screen.fill((0, 0, 0))
        for but in buttons:
            buttons[but].show() 
        text_surf = font.render(text, True, (0, 0, 255))
        screen.blit(text_surf, text_surf.get_rect(center = (midw + 90, midh - 100)))
        pygame.display.flip()
        clock.tick(FPS)
def cut(a):
    v = []
    q = a[1]
    q = q[:20]
    if len(q) < 20:
        q += " " * (20 - len(q))
    v.append(q)

    q = a[0]
    q = format(float(q), ".6f")
    v.append(q)

    q = a[2]
    q = q[:13]
    if len(q) < 13:
        q += " " * (13 - len(q))
    v.append(q)
    return "       ".join(v)
def records():
    intro_text = ["УРОВЕНЬ        ВРЕМЯ ИГРЫ      ИМЯ ИГРОКА"]
    intro_text += [cut(e) for e in get_res()]
    intro_text += ["", 
                  "",
                  "",
                  "Для выхода в главное меню нажмите клавишу Esc"]
    
    
    get_page(intro_text)
def rules():
    intro_text = ["Правила:", "",
                  "Ракеты: v",
                  "Бомбы: b",
                  "Пушка: SPACE(ПРОБЕЛ)",  
                  "Вверх: w",
                  "Вниз: s",
                  "Увеличить обороты: d",
                  "Уменьшить обороты: a"
                  "", 
                  "",
                  "Для выхода в главное меню нажмите клавишу Esc"]
    get_page(intro_text)

    
def run(value):
    start_at = time.process_time()
    if value == "1":
        a = level1.run()
    elif value == "2":
        a = level2.run()
    elif value == "3":
        a = level3.run()
    elif value == "4":
        a = level4.run()
    elif value == "5":
        a = level5.run()
    if a is True:
        ended_at = time.process_time()
        write_res(str(ended_at - start_at), value, text)
def get_res():
    with open("Text/records.txt", mode="r") as f:
        return [e.split(";") for e in list(map(str.strip, f.readlines()))]
def write_res(res, level, name):
    vals = get_res()
    vals.append([res, level, name])
    dct = {"1":[], "2":[], "3":[], "4":[], "5":[]}
    for e in vals:
        dct[e[1]] += [e]
    new = []
    for e in dct:
        dct[e].sort()
        new.append(dct[e][-1])
        

    vals = new.copy()
      
    
    with open("Text/records.txt", mode="w") as f:
        f.writelines([";".join(e) + '\n' for e in vals])
def do(value):
    if value == "top":
        records()
    elif value == "rules":
        rules()
    else:
        run(value)
    
if __name__ == "__main__":
    start_screen()
    
    