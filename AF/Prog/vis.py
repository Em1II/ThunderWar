import pygame
class VIS:
    def __init__(self):
        ...
    def shut_fuck_up(self):
        stp_list = [3, 4, 5]
        for e in stp_list:
            pygame.mixer.Channel(e).pause()
    def game_over(self):
        self.shut_fuck_up()
        with open('Text/game_cond.txt', 'w') as f:
            f.write('F')

    def game_not_over(self):
        with open('Text/game_cond.txt', 'w') as f:
            f.write('T')
    def get_game_cond(self):
        with open('Text/game_cond.txt', 'r') as f:
            a = f.read()
        return a