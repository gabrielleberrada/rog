## imports

import pygame as pg
from random import randint
from itertools import product
import numpy as np

## constantes

WHITE = (255, 255, 255)
SIZE = 20
PIXEL_SIZE = 20

## initialisation de la fenêtre

screen= pg.display.set_mode((SIZE * PIXEL_SIZE, SIZE * PIXEL_SIZE))
screen.fill(WHITE)
pg.display.flip()

## initialisation de la MAP

MAP = np.full((20,20), None)

# - 
MAP[0][:8] = '-'
MAP[7][:8] = '-'
MAP[10][:4] = '-'
MAP[12][:4] = '-'
MAP[15][:11] = '-'
MAP[19][:11] = '-'
MAP[3][13:18] = '-'
MAP[19][13:18] = '-'
MAP[7][14:17] = '-'

# |
MAP[3:20, 13] = '|'
MAP[3:20, 17] = '|'
MAP[:8, 0] = '|'
MAP[:8, 7] = '|'
MAP[15:20, 0] = '|'
MAP[15:20, 10] = '|'
MAP[7:12, 9] = '|'
MAP[7:12, 12] = '|'

## jeu
running = True

while running:
#     if caption:
#         pg.display.set_caption(caption)
#         pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

pg.quit()