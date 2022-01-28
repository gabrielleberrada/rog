import numpy as np
from rog import *
from rog_tonio import *




class monstre :
    pass #A voir ce qui est nécessaire pour les monstres on en fait un seul

#Création de la matrice des objets
mat_obj = np.full((25,25), None)
names_obj = ['*','j','!','(','&','o','n']

for i in range(10) :
    new_obj = np.random.choice(names_obj) # on choisit un objet au hasard
    i,j,state = np.random.choice(DOTS) #on choisit un triplet dans la liste de Tonio
    while state == 1 : #si la place est déjà occupée
         i,j,state = np.random.choice(DOTS)
    mat_obj[i,j] = new_obj  



sac = {'taille' : 0, 'vie': 10, 'portefeuille' : 0}
taille_max = 5

class Objet :
    """prend un objet avec un nom (str affiché sur la map), un type (arme, armure...)
    """
    def __init__(self, name):
        self.name = name #un array d'une lettre
         #On rajoute un num ????

    def take(self, Prendre = True) : #Pour l'instant on prend les pièces une par une à voir comment on fait pour le nombre
        pris = False
        if sac['taille'] >= taille_max :
            pass
        if self.name == '*':
            sac['portefeuille']+=1
            mat_obj[x_position, y_position] = None
            #Modification de la matrice objet
            new_obj = np.random.choice(names_obj) 
            i,j,state = np.random.choice(DOTS) 
            while state == 1 : 
                i,j,state = np.random.choice(DOTS)
            mat_obj[i,j] = new_obj 
            return sac
        caption = "Prendre l'objet Y/N?" #voir comment il répond et comment interagir
        if Prendre == True :
            if self.name == 'j': #potion magique qui remet la vie à 10 points
                sac['vie'] = 10
            elif self.name in sac :            
                sac[self.name] += 1
                sac['taille']+= 1
            else : 
                sac[self.name] = 1
            mat_obj[x_position, y_position] = None
            new_obj = np.random.choice(names_obj) # on choisit un objet au hasard
            i,j,state = np.random.choice(DOTS) #on choisit un triplet dans la liste de Tonio
            while state == 1 : #si la place est déjà occupée
                i,j,state = np.random.choice(DOTS)
            mat_obj[i,j] = new_obj 
