## imports

from xml.etree.ElementTree import PI
import pygame as pg
import random
from random import randint
from itertools import product
import numpy as np
import secrets

## constantes

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (186, 0, 0)
BEIGE = (169, 149, 123)
CERULEAN = (42, 82, 190)
SIZE = 25
PIXEL_SIZE = 20

## affichage de caractères
def draw_char(text, position, font, color=BLACK, background=WHITE):
    return font.render(text, False, color, background), position

## initialisation du sac
sac = {'taille' : 0, 'vie': 10, 'argent' : 0}
taille_max = 5
 

## initialisation de la MAP et de DOTS

MAP = np.full((25,50), None)

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
MAP[17, 11] = '+'
MAP[4, 8] = '+'

MAP = np.transpose(MAP)

DOTS = np.full((25,25), None)
for (i, j) in product(range(21), range(21)):
    if MAP[i, j] in ['.','#'] :
        DOTS[i,j] = 1
    
    

#Création de la matrice des objets
mat_obj = np.full((25,25), None)
names_obj = ['*','j','!','(','&','o']

for k in range(10) :
    new_obj = secrets.choice(names_obj) # on choisit un objet au hasard
    i,j = randint(0, 24), randint(0, 24) #on choisit un triplet dans la liste de Tonio
    while DOTS[i,j] != 1 : #si la place est déjà occupée ou non accessible
         i,j = randint(0, 24), randint(0, 24)
    mat_obj[i,j] = new_obj
    DOTS[i,j] = 0 #La place est occupée

## Classes Objets et monstres
class Objet :
    """prend un objet avec un nom (str affiché sur la map), un type (arme, armure...)
    """
    def __init__(self, name):
        self.name = name #un array d'une lettre
         #On rajoute un num ????

    def take(self, Prendre) : #Pour l'instant on prend les pièces une par une à voir comment on fait pour le nombre
        if sac['taille'] >= taille_max :
            return None
        if self.name == '*':
            sac['argent']+=1
            mat_obj[x_position, y_position] = None
            DOTS[x_position, y_position] = 1
            #Modification de la matrice objet
            new_obj = secrets.choice(names_obj) # on choisit un objet au hasard
            i,j = randint(0, 24), randint(0, 24) #on choisit un triplet dans la liste de Tonio
            while DOTS[i,j] != 1 : #si la place est déjà occupée ou non accessible
                i,j = randint(0, 24), randint(0, 24)
            mat_obj[i,j] = new_obj
            DOTS[i,j] = 0 #La place est occupée
            
        if Prendre == True :
            if self.name == 'j': #potion magique qui remet la vie à 10 points
                sac['vie'] = 10
            elif self.name in sac :            
                sac[self.name] += 1
                sac['taille']+= 1
            else :
                sac[self.name] = 1
                sac['taille']+=1
            mat_obj[x_position, y_position] = None
            DOTS[x_position, y_position] = 1
            new_obj = secrets.choice(names_obj) # on choisit un objet au hasard
            i,j = randint(0, 24), randint(0, 24) #on choisit un triplet dans la liste de Tonio
            while DOTS[i,j] != 1 : #si la place est déjà occupée ou non accessible
                i,j = randint(0, 24), randint(0, 24)
            mat_obj[i,j] = new_obj
            DOTS[i,j] = 0 #La place est occupée

class Monstre :
    """
    args : power (1 or 2) whether it's a small (m) or big (M) monster
    """
    def __init__(self, power, x_pos, y_pos):
        if power == 1:
            self.proba = 0.5
            self.name = 'm'
        if power == 2:
            self.proba = 0.2
            self.name = 'M'
        self.x_pos = x_pos
        self.y_pos = y_pos

    def fight(self):
        succes = random.uniform(0, 1)
        if '!' in sac.keys() and sac['!'] >= 1:
            succes += 0.2
            sac['!'] -= 1
        if '(' in sac.keys() and sac['('] >= 1:
            succes += 0.1
            sac['('] -= 1
        if succes <= self.proba: #fight lost
            if '&' in sac.keys() and sac['&'] >= 1:
                sac['vie'] -= 3
                sac['&'] -= 1
            else:
                sac['vie'] -= 5
        else: #fight won
            sac['argent'] += 3
        x_pos, y_pos = np.random.randint(25), np.random.randint(25)
        while not(DOTS[x_pos, y_pos]) or (x_pos == x_position and y_pos == y_position):
            x_pos, y_pos = np.random.randint(25), np.random.randint(25)
        self.x_pos = x_pos
        self.y_pos = y_pos
            
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

## mouvements

def authorized_movement(x_position, y_position, mvmt, map=MAP):
    if mvmt == 'up':
        if y_position and map[x_position, y_position - 1] in accessible_pos:
            return True
        return False
    if mvmt == 'down':
        if y_position < SIZE - 1 and map[x_position, y_position + 1] in accessible_pos:
            return True
        return False
    if mvmt == 'left':
        if x_position and map[x_position - 1, y_position] in accessible_pos:
            return True
        return False
    if mvmt == 'right': 
        if x_position < SIZE - 1 and map[x_position + 1, y_position] in accessible_pos:
            return True
        return False

def monster_moves(monster, map=MAP):
    x = monster.x_pos
    y = monster.y_pos
    mvmt = np.random.choice(['up', 'down', 'left', 'right'])
    while not(authorized_movement(x, y, mvmt, map)):
        mvmt = np.random.choice(['up', 'down', 'left', 'right'])
    if mvmt == 'up': 
        return x, y - 1
    if mvmt == 'down':
        return x, y + 1
    if mvmt == 'left':
        return x - 1, y
    if mvmt == 'right':
        return x + 1, y

## graphisme
colors = {'wall' : BLACK, 'floor': BEIGE, 'empty': WHITE, 'road': BEIGE}

def draw_rect(i, j, color):
    rect = pg.Rect(i*PIXEL_SIZE, j*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE)
    pg.draw.rect(screen, color, rect)

def draw_set(colors=colors):
    for i, j in product(range(SIZE), range(SIZE)):
        if map[i, j] == '#':
            draw_rect(i, j, colors['road'])
        elif map[i, j] == '-' or map[i,j] == '|':
            draw_rect(i, j, colors['wall'])
        elif map[i, j] == '.':
            draw_rect(i, j, colors['floor'])

## jeu
running = True
caption = 'Play ROG game'
count = 0
monsters = [Monstre(1, 3, 4), Monstre(1, 18, 5), Monstre(2, 14, 15)]

while running:
    screen.fill(WHITE)
    clock.tick(4)
    # affichage plateau de jeu
    draw_set()
    for i, j in product(range(SIZE), range(SIZE)):
        if i == x_position and j == y_position:
            img, pos = draw_char('@', ((i-0.3)*PIXEL_SIZE, j*PIXEL_SIZE), font=font_arial, color = RED)
            screen.blit(img, pos)
        elif mat_obj[i, j]:
            img, pos = draw_char(mat_obj[i,j], (i*PIXEL_SIZE, j*PIXEL_SIZE), font=font_arial, color = BEIGE)
            screen.blit(img, pos)
        # elif MAP[i,j]:
        #     img, pos = draw_char(MAP[i, j], (i*PIXEL_SIZE, j*PIXEL_SIZE), font=font_arial)
        #     screen.blit(img, pos)
        # img, pos = draw_char('inventaire', (1*PIXEL_SIZE, 21*PIXEL_SIZE), font=font_arial, color = BLACK)
        # screen.blit(img, pos)
    for i, elements in enumerate(sac.keys()):
        img, pos = draw_char(f"{elements}:{sac[elements]}", (5*i*PIXEL_SIZE, 23*PIXEL_SIZE), font=font_arial, color=BLACK)
        screen.blit(img, pos)
    # affichage messages
    if caption:
        pg.display.set_caption(caption)
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
            caption = "Prendre l'objet ? (press y)"
            pg.display.set_caption(caption)
            prendre = False
            if event.type == pg.KEYDOWN:
                caption = "Play ROG game" 
                pg.display.set_caption(caption)
                if event.key == pg.K_y:
                   prendre = True
            object.take(prendre) 
        else:
            caption = 'Play Rog Game'
            pg.display.set_caption(caption)
        for monster in monsters:
            if monster.x_pos == x_position and monster.y_pos == y_position:
                monster.fight()    
    for monster in monsters:
        img, pos = draw_char(monster.name, (monster.x_pos*PIXEL_SIZE, monster.y_pos*PIXEL_SIZE), font=font_arial, color = CERULEAN)
        screen.blit(img, pos)
        if not(count % 3):
            x, y = monster_moves(monster)
            monster.x_pos = x
            monster.y_pos = y
    count += 1
    if (x_position, y_position) == (2, 1):
        x_position, y_position = 10, 10
        caption = "T PIÉGÉ BOUFFON"
        pg.display.set_caption(caption)
    if sac['vie'] <= 0:
        running = False
        print("You lost the game")
    pg.display.update()


pg.quit()