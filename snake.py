#version finale avec argparse mais ici on ne peut mettre que l'argument de la taille

from random import randint
import pygame as pg
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("taillejeu", help="indiquer la taille du tableau de jeu")
#parser.add_argument("taillecase", help="indiquer la taille des cases du jeu")
args = parser.parse_args()
taille = args.taillejeu
#cases = args.taillecase

print(taille)
print(type(taille))

taille= int(taille)
print(taille)
print(type(taille))

cases = 20
carre= taille*cases
pg.init()
screen = pg.display.set_mode((carre, carre))
clock = pg.time.Clock()



# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
direction = (1, 0)
snake = [((taille//2)-1 , taille//2), (taille//2, taille//2), ((taille//2)+1, taille//2)]
fruit = (randint(0,taille - 1), randint(0, taille - 1))
score = 0
while running:

    clock.tick(2)
    for i in range(taille):
        for j in range(taille):
            rect= pg.Rect(i*cases, j*cases, cases, cases)
            pg.draw.rect(screen, (255*((i+j)%2),255*((i+j)%2),255*((i+j)%2)), rect)
    
    
    longueur = len(snake)
    

    for l in range(longueur):
        (i, j)= snake[l]
        rect= pg.Rect(i*cases, j*cases, cases, cases)
        pg.draw.rect(screen, (255, 0, 0), rect)

    
    if snake[-1] == fruit:
        tete = snake[-1]
        nouveau = (tete[0] + direction[0], tete[1] + direction[1])
        snake.append(nouveau)
        fruit = (randint(0, taille - 1), randint(0, taille - 1))
        score +=1
    else: 
        tete = snake[-1]
        snake = snake[1:]
        nouveau = (tete[0] + direction[0], tete[1] + direction[1])
        snake.append(nouveau)

    #dessin du fruit   
    rectfruit = pg.Rect(fruit[0]*cases, fruit[1]*cases, cases, cases)
    pg.draw.rect(screen, (0, 255, 255), rectfruit)


    #message fin du jeu avec un ecran rouge
    erreur = pg.Rect(0, 0, carre, carre)

    #tests d'erreurs de fin de jeu
    tete = snake[-1]
    if tete in snake[:-2]:
        pg.draw.rect(screen, (255, 0, 0), erreur)
        snake = [(taille, taille)]
        direction = (0, 0)
    elif (tete[0] in (-1, taille)) or (tete[1] in (-1, taille)):
        pg.draw.rect(screen, (255, 0, 0), erreur)
        snake = [(taille, taille)]
        direction = (0, 0)
    pg.display.update()
    pg.display.set_caption(f"Score: {score}")

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False
            elif event.key == pg.K_UP:
                if direction[0] != 0:
                    direction = (0, -1)
            elif event.key == pg.K_DOWN:
                if direction[0] != 0:
                    direction = (0, 1)
            elif event.key == pg.K_RIGHT:
                if direction[1] != 0:
                    direction = (1, 0)
            elif event.key == pg.K_LEFT:
                if direction[1] != 0:
                    direction = (-1, 0)

# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()

#notes

#VITESSE DE REACTION si on acceler le jeu le temps de reponse
#rend le jeu injouable
#en revanche si on repasse à 1 image/seconde on ne peut pas fermer instantanement 
#il faudrait desynchronise le jeu et les touches quit