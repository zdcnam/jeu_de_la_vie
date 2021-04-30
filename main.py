import pygame
import sys
from jeu_fenetre_class import *
from bouton_class import *

#Definition des constantes

WIDTH, HEIGHT = 800,800
BACKGROUND =  (199,199,199)
#vitesse d'evolution des generations
image_par_seconde = 60
 

#retourner une liste des evenements d'après la premiere fois d'etre appelé

#-------------------les fonctions de l'état initial----------------------------------------#
def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pointeur_position  = pygame.mouse.get_pos()
            if pointeur_sur_grille(pointeur_position):
                cliquer_cellule(pointeur_position)
            else:
                for bouton in boutons:
                    bouton.cliquer()



def update():
    jeu_fenetre.update()
    for bouton in boutons:
        bouton.update(pointeur_position, game_etat=etat)

def draw():
    fenetre.fill(BACKGROUND)
    for bouton in boutons:
        bouton.draw()
    jeu_fenetre.draw()


#-------------------les fonctions de l'état en fonction----------------------------------------#

def running_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pointeur_position  = pygame.mouse.get_pos()
            if pointeur_sur_grille(pointeur_position):
                cliquer_cellule(pointeur_position)
            else:
                for bouton in boutons:
                    bouton.cliquer()


  
def running_update():
    jeu_fenetre.update()
    for bouton in boutons:
        bouton.update(pointeur_position, game_etat=etat)
    if frame_count%(image_par_seconde/10) == 0:
        jeu_fenetre.appliquer_regles()
    
def running_draw():
    fenetre.fill(BACKGROUND)
    for bouton in boutons:
        bouton.draw()
    jeu_fenetre.draw()


#-------------------les fonctions de l'état en arret----------------------------------------#

def paused_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pointeur_position  = pygame.mouse.get_pos()
            if pointeur_sur_grille(pointeur_position):
                cliquer_cellule(pointeur_position)
            else:
                for bouton in boutons:
                    bouton.cliquer()



def paused_update():
    jeu_fenetre.update()
    for bouton in boutons:
        bouton.update(pointeur_position, game_etat=etat)

def paused_draw():
    fenetre.fill(BACKGROUND)
    for bouton in boutons:
        bouton.draw()
    jeu_fenetre.draw()

#La position du pointeur de la souris
def pointeur_sur_grille(pos):
    if pos[0] > 100 and pos[0] < WIDTH-100:
        if pos[1] > 180 and pos[1] < HEIGHT - 20:
            return True
    return False

def cliquer_cellule(pos):
    grille_pos = [pos[0] -100, pos[1] -180]
    grille_pos[0] = grille_pos[0]//20
    grille_pos[1] = grille_pos[1]//20

    #cliquer sur une cellule pour mettre morte ou vivante 
    if jeu_fenetre.grille[grille_pos[1]][grille_pos[0]].alive:
        jeu_fenetre.grille[grille_pos[1]][grille_pos[0]].alive = False
    else:
        jeu_fenetre.grille[grille_pos[1]][grille_pos[0]].alive = True


#Créer des boutons pour gérer les differents états du jeu
def make_boutons():
    boutons = []
    boutons.append(Bouton(fenetre, WIDTH//2-50, 50, 100, 30, text='Lancer',
    colour=(200,200, 255), hover_colour=(48,140,81), text_colour=(0,0,0), bold_text=True, function=lancer_jeu, etat='initial'))

    boutons.append(Bouton(fenetre, WIDTH//2-50, 50, 100, 30, text='ARRETER',
    colour=(200,200, 255), hover_colour=(48,140,81), text_colour=(0,0,0) ,bold_text=True, function=arreter_jeu, etat='en_fonction'  ))

    boutons.append(Bouton(fenetre, WIDTH//4.5-50, 55, 121, 35, text='REINITIALISER',
    colour=(200,200, 255), hover_colour=(48,140,81), text_colour=(0,0,0),bold_text=True, function=reinitialiser_grille, etat='en_arret'))

    boutons.append(Bouton(fenetre, WIDTH//1.2-50, 50, 100, 30, text='RESUMER',
    colour=(200,200, 255), hover_colour=(48,140,81), text_colour=(0,0,0),bold_text=True, function=lancer_jeu, etat='en_arret'))


    return boutons

def lancer_jeu():
    global etat
    etat = 'en_fonction'
    

def arreter_jeu():
    global etat
    etat = 'en_arret'
 
def reinitialiser_grille():
    global etat
    etat = 'initial'
    jeu_fenetre.reinitialiser_grille()

pygame.init()
fenetre = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
jeu_fenetre = Jeu_fenetre(fenetre, 100, 180)


boutons = make_boutons()
etat='initial'
frame_count =0
running = True

while running:
    frame_count +=1
    pointeur_position = pygame.mouse.get_pos()
    if etat == 'initial':
        get_events()
        update()
        draw()
        

    if etat == 'en_fonction':
        running_get_events()
        running_update()
        running_draw()

    if etat == 'en_arret':
        paused_get_events()
        paused_update()
        paused_draw()

    
    pygame.display.update()
    clock.tick(image_par_seconde)

pygame.quit()