
## imports

import pygame as pg
from random import randint
from itertools import product
import numpy as np

## constantes

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SIZE = 25
PIXEL_SIZE = 30

import numpy as np

MAP = np.full((25,25), None)

# |
MAP[3:20, 14] = '|'
MAP[3:20, 18] = '|'
MAP[:8, 1] = '|'
MAP[:8, 8] = '|'
MAP[15:20, 1] = '|'
MAP[15:20, 11] = '|'
MAP[9:14, 9] = '|'
MAP[9:14, 12] = '|'
MAP[10:13, 1] = '|'
MAP[10:13, 4] = '|'

# - 
MAP[0][1:9] = '-'
MAP[7][1:9] = '-'
MAP[10][1:5] = '-'
MAP[12][1:5] = '-'
MAP[15][1:12] = '-'
MAP[19][1:12] = '-'
MAP[3][14:19] = '-'
MAP[19][14:19] = '-'
MAP[7, 15:18] = '-'
MAP[9, 9:13] = '-'
MAP[13, 9:13] = '-'

# sol
MAP[1:7, 2:8] = '.'
MAP[11, 2:4] = '.'
MAP[16:19, 2:11] = '.'
MAP[4:7, 15:18] = '.'
MAP[8:19, 15:18] = '.'
MAP[10:13, 10:12] = '.'


# chemin
MAP[8:11, 6] = '#'
MAP[11, 5:8] = '#'
MAP[11:15, 7] = '#'
MAP[17, 12:14] = '#'
MAP[2, 11:17] = '#'
MAP[2:5, 11] = '#'
MAP[4, 8:12] = '#'

# porte
MAP[7, 6] = '+'
MAP[11, 4] = '+'
MAP[15, 7] = '+'
MAP[17, 14] = '+'
MAP[3, 16] = '+'
MAP[7,16] = '+'

MAP = np.transpose(MAP)

DOTS = []
for (i, j) in product(range(21), range(21)):
    if MAP[i, j] == '.':
        DOTS.append((i, j , 0))


## affichage de caractères
def draw_char(text, position, font, color=BLACK, background=WHITE):
    return font.render(text, False, color, background), position


## initialisation de la fenêtre

pg.init()
screen= pg.display.set_mode((SIZE * PIXEL_SIZE, SIZE * PIXEL_SIZE))
screen.fill(WHITE)
pg.display.flip()

## initialisation de la police
font_arial = pg.font.SysFont('arial', 20)

## jeu
running = True
caption = 'Play ROG game'

while running:
    # affichage plateau de jeu
    for i, j in product(range(SIZE), range(SIZE)):
        if MAP[i,j]:
            # what the fuck
            img, pos = draw_char(MAP[i,j], (i*PIXEL_SIZE, j*PIXEL_SIZE), font=font_arial)
            screen.blit(img, pos)
    # affichage messages
    if caption:
        pg.display.set_caption(caption)
        pg.display.flip()
    # itération sur tous les événements
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False

    pg.display.update()


pg.quit()