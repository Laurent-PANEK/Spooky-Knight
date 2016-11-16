#-*-coding:utf8-*-
"""
    on importe tous les modules nécessaires.
"""
from tkinter import *
import PIL
import pygame
from pygame.locals import* #
import random
import time
from tkinter.messagebox import*
from math import*
import sys

pygame.init() # on initialise pygame
son1=pygame.mixer.Sound("MusiqueFondMenu.wav") # on définit la musique de fond ...
son1.set_volume(1.0) # ... puis son volume.
son2=pygame.mixer.Sound("kahvi173a_nedavine-dark_noon.wav") # on définit la musique du jeu ...
son2.set_volume(1.0) # ...puis son volume.

def music() :
    """
    fonction permettant de stopper le son.
    """
    global son,son1
    pygame.mixer.init()
    if son.get() == 1 :
        son1.play(-1)
    else:
        son1.stop()

def animMenu() :
    """
    fonction gérant l'apparition de l'animation du menu.
    """
    global can1
    can1.create_image(300,169,image=image0) # on crée la première image.
    Mafenetre.update() # on actualise la fenêtre.
    time.sleep(0.5) # on attend 0,5 seconde.
    can1.create_image(300,169,image=image1) # on crée la deuxième image.
    Mafenetre.update() # on actualise la fenêtre
    time.sleep(0.3) # on attend 0,3 seconde.
    can1.create_image(300,169,image=image2)
    Mafenetre.update()
    time.sleep(0.1)
    can1.create_image(300,169,image=image3)
    can1.create_image(300,169,image=titre)
    Mafenetre.update()


def quitte() :
    """
    fonction permettant de quitter le jeu proprement.
    """
    global son1
    pygame.mixer.init() # on initialise le module mixer.
    son1.stop() # on arrete la lecture du son1.
    Mafenetre.destroy() # on détruit la fenêtre du menu.

def menu():
    """
    fonction définissant l'affichage du menu.
    """
    global val,son,can1

    can1=Canvas(Mafenetre,width=600,height=337) # on crée le canvas can1 dans la fenêtre Mafenetre ...
    can1.place(x=0,y=0) # ... puis on indique sa position.
    bou1=Button(Mafenetre,image=quitter,command=quitte) # on crée le bouton bou1 qui sert à quitter la fenêtre en appelant la fonction quitte ...
    bou1.place(x=250,y=280) # ... puis on indique sa position.
    bou3=Button(Mafenetre,image=photoStart,command=choixJeu) # on crée le bouton bou3 qui appelle la fonction choixJeu ...
    bou3.place(x=20,y=240) # ... puis on indique sa position.
    bou4=Button(Mafenetre,image=photoOptions,command=option) # on crée le bouton bou4 qui appelle la fonction option ...
    bou4.place(x=440,y=240) # ... puis on indique sa position
    music() # on appelle la fonction music.
    animMenu() # on appelle la fonction animMenu.

def difficulte () :
    """
    fonction permettant de changer la difficulté du jeu.
    """
    global Temps,val,D

    v=int(val.get()) # on récupre la valeur de la variable val a l'aide de .get() que l'on attribut à v.

    if v == 1 : # si v est égale à 1, on considère la difficulté du jeu comme facile.
        Temps = 30
        D=2
    elif v == 2 : # si v est égale à 2, la difficulté du jeu est difficle.
        Temps = 60
        D=3
    elif v == 3 : # si v est égale à 3, la fifficulté du jeu est TRES difficile.
        Temps = 120
        D=5
    else : # par défaut la difficulté est facile.
        Temps = 100
        D=3

def choixJeu() :
    """
    fonction principale où le jeu est executé
    """
    import classgagam_test # on importe les 3 fichier nécessaires au fonctionnement du jeu.
    import constantegagam
    import ennemy_test
    global son,son1,fenetre,t1,t2,n,Temps,val,Vie,D
    pygame.mixer.init() # on initialise le module mixer.
    son1.stop() # on arrête la lecture du son1.
    son2.play(-1) # on lis le son2 de façon infini.
    dimensions=(1000,480) # on définit les dimensions de la fenêtre.
    fenetre=constantegagam.fenetre # on définit la fenêtre comme étant celle du fichier constantegagam...
    pygame.display.set_icon(constantegagam.icon) # de même pour l'icone de la fenêtre ...
    pygame.display.set_caption(constantegagam.title) # ... et son titre.
    sheet=constantegagam.sheet # on définit le sprite du personnage.
    fond=constantegagam.fond # on définit le fond.

    perso=classgagam_test.Perso(fenetre,fond,(20,50),sheet,True) # on définit le personnage comme étant la classe Perso du fichier classgagam_test
    perso.idle() # on appelle le module de la classe Perso.
    clock = pygame.time.Clock() # on définit l'horloge de la fenêtre.
    posx=10 # on initialise la position x du personnage.
    posy=480-94 # on initialise la position y du personage.
    difficulte() # on appelle la fonction difficulte pour récupérer les variables qui ont potentiellement changées.
    classgagam_test.n = Temps # on définit la variable n comme étant égale à  la variable Temps, issue de difficulte.
    classgagam_test.difficulte = D # on définit la variable difficulte comme étant égale à  la variable D, issue de difficulte.
    pygame.display.flip() # on rafraîchit l'écran.

    side=1 # initialisation de la variable side.
    grav=0 # initialisation de la variable de gravité.
    direc=0 # initialiation de la varialbe de direction.
    continuer=1 # initialisation de la variable de la boucle infini.
    ani=0 # initialisation de la variable d'animation
    pygame.key.set_repeat(100,17) # permet de pas surcharger le programme en attendant 100 ms entre chaque action identique.
    while continuer: # boucle infinie.

        onground=perso.gravity(grav,side) # initialisation de la gravité du personnage.
        clock.tick(60) # définit le nombre d'image par seconde.

        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE: # si la touche échap est pressé, son2 est arrêté et la boucle prend fin.
                    pygame.mixer.init()
                    son2.stop()
                    continuer=0

                if event.key==K_RIGHT: # si la flèche directionnelle droite est pressée ...

                    side=1
                    grav=2

                    if onground==True:

                        perso.move(3) # ... le personnage avance à droite s'il est sur le sol ...

                    elif onground==False:

                        onground=perso.gravity(grav,side) # ... sinon il est soumis à la gravité.

                    direc=1

                if event.key==K_LEFT: # si la flèche directionnelle gauche est pressée ...

                    side=3
                    grav=-2
                    if onground==True:

                        perso.move(-3) # ... le personnage avance à gauche s'il est sur sol ...

                    elif onground==False:

                        onground=perso.gravity(grav,side) # ... sinon il est soumis à la gravité.

                    direc=-1


                if event.key==K_SPACE: # si le bouton espace est pressé ...

                    perso.jump(direc,side) # ... le personnage saute.

                if event.key==K_x: # si le bouton x est pressé ...

                    perso.combo(grav,side) # ... le personnage attaque

                if event.key==K_r: # si le bouton r est pressé ...
                    pygame.mixer.init()
                    continuer=0 # ... on sort de la boucle ...
                    son2.stop() # ... on arrête la lecture du son2 ...
                    constantegagam.point = 0 # ... on réinitialise le score ...
                    classgagam_test.nb_vie = 3 # ... on réinitialise la vie ...
                    classgagam_test.deft = False # ... on réinitialise la variable comptant la défaite ...
                    classgagam_test.vic = False # ... on réinitialise la variable comptant la victoire ...
                    choixJeu() # ... et on relance la fonction choixJeu.
    pygame.quit() # on ferme pygame.


def option() :
    """
    fonction permettant l'affiche des commandes et options.
    """
    global val,son,can2,Temps
    can2=Canvas(Mafenetre,width=600,height=337,bg='#d40404') # on crée un canvas can2 où sera affiché toutes les informations.
    can2.place(x=0,y=0)
    bou1=Button(Mafenetre,image=quitter,command=menu) # on crée un boutton pour revenir au menu.
    bou1.place(x=250,y=280)
    can2.create_text(300,20,text="Serez-vous capable de survivre face ",font="Fipps 12") # on crée des textes pour afficher les informations.
    can2.create_text(300,45,text=" aux inombrables ennemies que  ",font="Fipps 12")
    can2.create_text(300,70,text="devra combattre Spooky ?!  ",font="Fipps 12")
    can2.create_text(300,95,text="Déplacez-vous avec les flêches directionnelles",font="Fipps 11")
    can2.create_text(300,115,text="Sautez avec la touche Espace.",font="Fipps 11")
    can2.create_text(300,135,text="Défendez-vous avec la touche X.",font="Fipps 11")
    can2.create_text(300,155,text="Recommencez avec la touche R.",font="Fipps 11")
    can2.create_text(300,175,text="Quittez avec Echap.",font="Fipps 11")

    Checkbutton(Mafenetre,text='Son',variable=son,command=music,bg='#d40404').place(x=250,y=190) # on crée un boutton à case qui sert à contrôler la présence du son.

    lvl1=Radiobutton(Mafenetre,text='Niveau Facile',variable=val,value=1,bg='#d40404',command=difficulte).place(x=250,y=210) # on crée un radio bouton pour définir le niveau.
    lvl2=Radiobutton(Mafenetre,text='Niveau Difficile',variable=val,value=2,bg='#d40404',command=difficulte).place(x=250,y=230)
    lvl3=Radiobutton(Mafenetre,text='Niveau HARDCORE ',variable=val,value=3,bg='#d40404',command=difficulte).place(x=250,y=250)

Mafenetre = Tk()    # creation d'une fenêtre windows.
Mafenetre.geometry('600x337') # initialisation des dimensions de la fenêtre.
Mafenetre.title('Spooky Knight - Specialite ISN - Version 1.0.0') # initialisation du titre de la fenêtre ...
Mafenetre.iconbitmap("image/sk.ico") # ... et de son icône.
#Mafenetre.wm_state(newstate="zoomed")
Mafenetre.resizable(width=False, height=False) # on définit la fenêtre pour que l'utilisateur ne puisse pas la redimensionner.

# initialisation des images utilisé dans le menu.
photo=PhotoImage(file="image/imgMenuJeu.gif")
photoStart=PhotoImage(file="image/bouton1.gif")
photoOptions=PhotoImage(file="image/bouton2.gif")
quitter=PhotoImage(file="image/imgExitv3.gif")
image0=PhotoImage(file="image/spookyknight0.gif")
image1=PhotoImage(file="image/spookyknight1.gif")
image2=PhotoImage(file="image/spookyknight2.gif")
image3=PhotoImage(file="image/spookyknight3.gif")
titre=PhotoImage(file="image/titreMenu.gif")

# initialisatin des variables modifiables avec un boutton.
val=IntVar()
val.set(1)
son=IntVar()
son.set(1)

# appel de la fonction menu.
menu()

#on envoie le tout
Mafenetre.mainloop()
