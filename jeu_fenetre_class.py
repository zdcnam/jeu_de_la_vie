import pygame
from cellule_class import *
vec = pygame.math.Vector2
import copy


class Jeu_fenetre:
    def __init__(self, screen, x, y):
        self.screen =screen
        self.pos = vec(x,y)
        self.width, self.height = 600, 600
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rows = 30
        self.cols = 30

        self.grille= [[Cellule(self.image, x,y) for x in range(self.cols)] for y in range(self.rows)]
        for row in self.grille:
            for cell in row:
                cell.get_voisins(self.grille)
    
    def update(self):

        self.rect.topleft = self.pos
        for row in self.grille:
            for cell in row:
                cell.update()

    def draw(self):
        self.image.fill((102, 102, 102))
        for row in self.grille:
            for cell in row:
                cell.draw()
        self.screen.blit(self.image, (self.pos.x, self.pos.y))

    def reinitialiser_grille(self):
        self.grille= [[Cellule(self.image, x,y) for x in range(self.cols)] for y in range(self.rows)]        
        #self.grille = copy.copy(self.grille)
        for row in self.grille:
            for cell in row:
                cell.get_voisins(self.grille)


    #appliquer les règles de jeu de la vie pour avoir une nouvelle géneration
    def appliquer_regles(self):
        new_grille = copy.copy(self.grille)

        for row in self.grille:
            for cell in row:
                cell.live_voisins()
        #Utilisation de enumarate car elle retourne tuple avec comteur et valeur
        for ydix, row in enumerate(self.grille):
            for xidx, cell in enumerate(row):
                if cell.alive:
                    if cell.alive_voisins == 2 or cell.alive_voisins == 3:
                        new_grille[ydix][xidx].alive = True
                    if cell.alive_voisins < 2:
                        new_grille[ydix][xidx].alive = False
                    if cell.alive_voisins > 3:
                        new_grille[ydix][xidx].alive = False
                else:
                    if cell.alive_voisins == 3:
                        new_grille[ydix][xidx].alive = True

