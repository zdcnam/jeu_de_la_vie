import pygame, random

class Cellule:
    def __init__(self, surface, grille_x, grille_y):
        self.alive = False
        self.grille_x=  grille_x
        self.grille_y = grille_y
        self.surface = surface
        self.image = pygame.Surface((20,20))
        self.rect = self.image.get_rect()
        self.voisins = []
        self.alive_voisins = 0

    def update(self):
        self.rect.topleft = (self.grille_x*20, self.grille_y*20)
       

    def draw(self):
        if self.alive:
            self.image.fill((0,0,0))
        else:
            self.image.fill((0,0,0))
            pygame.draw.rect(self.image, (255,255,255), (1,1,18,18))
        self.surface.blit(self.image,( self.grille_x*20, self.grille_y*20))
    

    def get_voisins(self, grille):
        voisin_list = [[0,1], [0,-1], [1,0] , [1,1], [1,-1], [-1,0] , [-1,1] ,[-1,-1]]
        for voisin in voisin_list:
            voisin[0] += self.grille_x
            voisin[1] += self.grille_y
        for voisin in voisin_list:
            if voisin[0] < 0 :
                voisin[0] += 30
            if voisin[1] < 0:
                voisin[1] += 30
            if voisin[1] > 29:
                voisin[1] -= 30
            if voisin[0] > 29:
                voisin[0] -= 30
        for voisin in voisin_list:
            try:
                self.voisins.append(grille[voisin[1]][voisin[0]])
            except:
                print(voisin)  

    def live_voisins(self):
        count=0
        for voisin in self.voisins:
            if voisin.alive:
                count += 1
        self.alive_voisins = count

    