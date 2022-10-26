# v1 : pareil mais au moins on peut sortir du programme
# avec la touche 'q', ou avec la souris en fermant la fenêtre

from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()



# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
direction = (1, 0)
snake = [(10, 15), (11, 15), (12, 15)]
fruit = (randint(0,29), randint(0, 29))
score = 0
while running:

    clock.tick(2)
    for i in range(30):
        for j in range(30):
            rect= pg.Rect(i*20, j*20, 20, 20)
            pg.draw.rect(screen, (255*((i+j)%2),255*((i+j)%2),255*((i+j)%2)), rect)
    
    
    longueur = len(snake)
    

    for l in range(longueur):
        (i, j)= snake[l]
        rect= pg.Rect(i*20, j*20, 20, 20)
        pg.draw.rect(screen, (255, 0, 0), rect)

    #creation du fruit
   
    
    if snake[-1] == fruit:
        tete = snake[-1]
        nouveau = (tete[0] + direction[0], tete[1] + direction[1])
        snake.append(nouveau)
        fruit = (randint(0, 29), randint(0, 29))
        score +=1
    else: 
        tete = snake[-1]
        snake = snake[1:]
        nouveau = (tete[0] + direction[0], tete[1] + direction[1])
        snake.append(nouveau)
        
    rectfruit = pg.Rect(fruit[0]*20, fruit[1]*20, 20, 20)
    pg.draw.rect(screen, (0, 255, 255), rectfruit)


    #message fin du jeu
    erreur = pg.Rect(0, 0, 600, 600)

    tete = snake[-1]
    if tete in snake[:-2]:
        pg.draw.rect(screen, (255, 0, 0), erreur)
        snake = [(30, 30)]
        direction = (0, 0)
    elif (tete[0] in (-1, 30)) or (tete[0] in (-1, 30)):
        pg.draw.rect(screen, (255, 0, 0), erreur)
        snake = [(30, 30)]
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