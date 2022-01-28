## imports

import pygame as pg
from random import randint
from itertools import product
import numpy as np
import secrets

## constantes

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SIZE = 25
PIXEL_SIZE = 20
RED = (186, 0, 0)
BEIGE = (169, 149, 123)

## affichage de caractères
def draw_char(text, position, font, color=BLACK, background=WHITE):
    return font.render(text, False, color, background), position

## initialisation du sac
sac = {'taille' : 0, 'vie': 10, 'portefeuille' : 0}
taille_max = 5
 

## initialisation de la MAP et de DOTS

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
        DOTS.append((i, j,0))

#Création de la matrice des objets
mat_obj = np.full((25,25), None)
names_obj = ['*','j','!','(','&','o','n']

for i in range(10) :
    new_obj = secrets.choice(names_obj) # on choisit un objet au hasard
    i,j,state = secrets.choice(DOTS) #on choisit un triplet dans la liste de Tonio
    while state == 1 : #si la place est déjà occupée
         i,j= secrets.choice(DOTS)
    mat_obj[i,j] = new_obj

## Classes Objets et monstres
class Objet :
    """prend un objet avec un nom (str affiché sur la map), un type (arme, armure...)
    """
    def __init__(self, name):
        self.name = name #un array d'une lettre
         #On rajoute un num ????

    def take(self, Prendre = True) : #Pour l'instant on prend les pièces une par une à voir comment on fait pour le nombre
        if sac['taille'] >= taille_max :
            pass
        if self.name == '*':
            sac['portefeuille']+=1
            mat_obj[x_position, y_position] = None
            #Modification de la matrice objet
            new_obj = secrets.choice(names_obj) 
            i,j,state = secrets.choice(DOTS) 
            while state == 1 : 
                i,j,state = secrets.choice(DOTS)
            mat_obj[i,j] = new_obj 
            pass
        caption = "Prendre l'objet? Y/N" #voir comment il répond et comment interagir
        if Prendre == True :
            if self.name == 'j': #potion magique qui remet la vie à 10 points
                sac['vie'] = 10
            elif self.name in sac :            
                sac[self.name] += 1
                sac['taille']+= 1
            else : 
                sac[self.name] = 1
            mat_obj[x_position, y_position] = None
            new_obj = secrets.choice(names_obj) # on choisit un objet au hasard
            i,j,state = secrets.choice(DOTS) #on choisit un triplet dans la liste de Tonio
            mat_obj[i,j] = new_obj
            
## initialisation de la fenêtre

pg.init()
clock = pg.time.Clock()
screen= pg.display.set_mode((SIZE * PIXEL_SIZE, SIZE * PIXEL_SIZE))
pg.display.flip()


## initialisation de la police
font_arial = pg.font.SysFont('arial', 20)

## initialisation de la position
x_position = 2
y_position = 5

## points accessibles
accessible_pos = ['.', '+', '#']


## jeu
running = True
caption = 'Play ROG game'

while running:
    screen.fill(WHITE)
    clock.tick(4)
    # affichage plateau de jeu
    for i, j in product(range(SIZE), range(SIZE)):
        if i == x_position and j == y_position:
            img, pos = draw_char('@', ((i-0.3)*PIXEL_SIZE, j*PIXEL_SIZE), font=font_arial, color = RED)
            screen.blit(img, pos)
        elif mat_obj[i, j]:
            img, pos = draw_char(mat_obj[i,j], (i*PIXEL_SIZE, j*PIXEL_SIZE), font=font_arial, color = BEIGE)
            screen.blit(img, pos)
        elif MAP[i,j]:
            # what the fuck
            img, pos = draw_char(MAP[i, j], (i*PIXEL_SIZE, j*PIXEL_SIZE), font=font_arial)
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
            elif event.key == pg.K_UP:
                # on reste dans le screen et on peut accéder à la case
                if y_position and MAP[x_position, y_position - 1] in accessible_pos:
                    y_position -= 1
            elif event.key == pg.K_DOWN:
                if y_position < SIZE - 1 and MAP[x_position, y_position + 1] in accessible_pos:
                    y_position += 1
            elif event.key == pg.K_LEFT:
                if x_position and MAP[x_position - 1, y_position] in accessible_pos:
                    x_position -= 1
            elif event.key == pg.K_RIGHT:
                if x_position and MAP[x_position + 1, y_position] in accessible_pos:
                    x_position += 1
        if mat_obj[x_position, y_position]:
            object = Objet(mat_obj[x_position, y_position])
            object.take()

    pg.display.update()


pg.quit()## imports