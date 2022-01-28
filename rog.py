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