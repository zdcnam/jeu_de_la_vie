Déscription génerale de jeu de la vie

Le jeu de la vie se représente sur une grille de 2 dimensions composée des cellules qui ont un état  (Vivante|Live et Morte|Dead).
Le jeu de la vie est un automate cellulaire qui repose sur le principe d'évolution de la grille dans le temps. A chaque étape, appelée génération, les cellules évoluent en fonction de leur voisinage (chaque cellule a 8 cellules voisines).


Les règles de la jeu de vie principale sont:

1- Chaque cellule possède 8 voisins
2- chaque cellule vivante possédant un nombre de voisins vivants inférieur à 2 devient MORTE dans la génération suivante
3- chaque cellule vivante possédant un nombre de voisins vivants supérieur à 3  devient MORTE dans la génération suivante
4- chaque cellule vivante possédant un nombre de voisins vivants 2 ou 3 rest VIVANTE dans la génération suivante
5- chaque cellule morte possédant un nombre de voisins vivant égale à 3 devient VIVANTE  dans la génération suivante


Description du programme

Le programme suivant consiste à appliquer le jeu de la vie avec la librairie graphique Pygame

- Grille est initialisé avec un width et height et background color

- Utilisation des 3 classes principale pour constituer le programme (Bouton, Cellule, jeu_fenetre)

- Le dynamique principale du programme est l'objet état qui represente l'état du programme et non pas la cellule

Etats
Dans ce programme on a 3 état pour definir le jeu de la vie: 

état initial (setting state)
état en fonction (running state)
état en pose (paused state)



