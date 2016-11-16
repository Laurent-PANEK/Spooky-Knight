#-*-coding:utf8-*-
"""
    on importe tous les modules nécessaires.
"""
import pygame
from pygame.locals import*
import time
import random
import constantegagam
import classgagam_test



class Ennemy (pygame.sprite.Sprite): # on définit la classe Ennemy
    global nb_vie
    def __init__(self,fenetre,fond,rect,sprite):
            pygame.sprite.Sprite.__init__(self)
            self.x=rect[0]
            self.y=rect[1]
            self.base=sprite
            self.fenetre=fenetre
            self.fond=fond

    def move(_x,_y):
        """
        fonction gérant les déplacement des ennemies.
        """
        for ennemy in constantegagam.ennemy_list :
            if ennemy[0] > _x : # si l'ennemie est à droit du personnage ...
                ennemy[0] -= 2 # ... il va à gauche.
            if ennemy[0] < _x : # si l'ennemie est à gauche du personnage ...
                ennemy[0] += 2 # ... il va à droite.
            if ennemy[1] < _y : # si l'ennemie est au-dessus du personnage ...
                ennemy[1] += 2 # ... il descend.
            if ennemy[1] > _y : # si l'ennemi est en-dessous du personnage ...
                ennemy[1] -= 2 # ... il monte.

    def genEnnemy() :
        """
        fonction gérant la génération aléatoire des ennemies.
        """
        if constantegagam.ennemy_number < classgagam_test.difficulte : # si le nombre maximale d'ennemie (lié à la difficulté) n'est pas atteint ...
            x=random.randint(20,950) # ... on génère un x ...
            y=random.randint(200,388) # ... et un y aléatoirement.
            constantegagam.x_y = [x,y] # on les met dans une liste, qui forme ainsi un couple de coordonnée.
            constantegagam.ennemy_list.append(constantegagam.x_y) # on ajoute cette liste dans une autre liste où tous les ennemies sont repertoriés.
            constantegagam.ennemy_number += 1 # on incrémente le nombre d'ennemie présent.

    def colli(_x,_y,dim) :
        """
        fonction gérant les collisions entre ennemies et personage
        """
        enm=[] # on définit une liste vide.
        perso = pygame.Rect(_x,_y,dim,dim) # on crée un rect qui à les coordonnées du personnage et une dimension variable selon l'animation.
        for ennemy in constantegagam.ennemy_list :
            enm.append(pygame.Rect(ennemy[0],ennemy[1],50,50)) # de même on crée un rect pour chaque ennemies que l'on place dans la liste définit précedemment.
        r = perso.collidelist(enm) # on utilise le paramètre collidelist spécifique au rect pour tester l'intersection entre deux rect, ici entre le rect du personnage et la liste de rect des ennemies.
        if r != -1 : # si la réponse est différente de -1 il y a une intersection.
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_x: # si la touche x est pressé...
                        del enm[r] # ... on supprime le rect ...
                        del constantegagam.ennemy_list[r] # ... et les coordonnées de l'ennemie touché ...
                        constantegagam.point += 10 # ... on ajoute 10 au score ...
                        constantegagam.ennemy_number -= 1 # ... et on décrémente le nombre d'ennemie.
                    else :
                        classgagam_test.nb_vie -= 1 # sinon on décrémente la vie du personnage...
                        return classgagam_test.nb_vie # qu'on retourne.

