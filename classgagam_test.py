#-*-coding:utf8-*-
"""
    on importe tous les modules nécessaires.
"""
import pygame
from pygame.locals import*
import time
import random
from math import floor
import constantegagam
import ennemy_test
import pickle

global ennemy,n,ennemy_list,nb_vie

# initialisation des variables utilisées dans plusieurs fichiers.
n=0
nb_vie=3
difficulte=0
deft=False
vic=False

pygame.init() # initialisation de pygame.

class Perso(pygame.sprite.Sprite): # définition de la classe Perso.

    global ennemy,n,nb_vie,difficulte,deft,vic

    def __init__(self,fenetre,fond,rect,sprite,playable):
        """
        fonction servant à initialiser tous les paramètres et variables de la classe.
        """
        global ennemy,n,nb_vie,difficulte

        pygame.sprite.Sprite.__init__(self)
        self.x=rect[0]
        self.y=rect[1]
        self.nature=playable
        self.dim = 100

        self.base=constantegagam.base
        self.frame=self.base
        self.fenetre=constantegagam.fenetre
        self.fond=fond

        self.onground=True
        self.dirmem=1
        self.ani=0

        self.gtime=0.9

        self.r=constantegagam.run_right
        self.l=constantegagam.run_left

        self.s=constantegagam.strike_right
        self.sl=constantegagam.strike_left

        self.airs=constantegagam.airstrike_right
        self.airsl=constantegagam.airstrike_left

        self.j1=pygame.image.load("image/spookyjump2.png").convert_alpha()
        self.j2=pygame.image.load("image/spookyjump3.png").convert_alpha()
        self.jl1=pygame.image.load("image/spookyjumpl2.png").convert_alpha()
        self.jl2=pygame.image.load("image/spookyjumpl3.png").convert_alpha()

        self.left=pygame.image.load("image/spookyleft3.png").convert_alpha()
        self.j=[self.j1,self.j2,self.jl1,self.jl2]

        self.speed=0.8
        self.rawspd=0
        self.fallspd=floor(2.21*self.gtime*self.gtime)
        self.jumpspd=7
        self.hit=0

        self.maxx=1000
        self.t1 = int = time.time ()
        self.t2 = 0

    def open_img(self,n):
        """
        fonction permettant l'affichage du temps.
        """
        nn=str(n)
        if int(nn) <= 300 and int(nn) >= 100 :
            img1 = pygame.image.load("image/"+nn[0]+" Timer.png").convert_alpha()
            self.fenetre.blit(img1, (0,0))
            img2 = pygame.image.load ("image/"+nn[1]+" Timer.png").convert_alpha()
            self.fenetre.blit(img2, (36,0))
            img3 = pygame.image.load ("image/"+nn[2]+" Timer.png").convert_alpha()
            self.fenetre.blit(img3, (72,0))
        elif int(nn) < 100 and int(nn) >= 10 :
            img1 = pygame.image.load("image/0 Timer.png").convert_alpha()
            self.fenetre.blit(img1, (0,0))
            img2 = pygame.image.load ("image/"+nn[0]+" Timer.png").convert_alpha()
            self.fenetre.blit(img2, (36,0))
            img3 = pygame.image.load ("image/"+nn[1]+" Timer.png").convert_alpha()
            self.fenetre.blit(img3, (72,0))
        elif n < 10 and n > 0 :
            img1 = pygame.image.load("image/0 Timer.png").convert_alpha()
            self.fenetre.blit(img1, (0,0))
            img2 = pygame.image.load ("image/0 Timer.png").convert_alpha()
            self.fenetre.blit(img2, (36,0))
            img3 = pygame.image.load ("image/"+nn[0]+" Timer.png").convert_alpha()
            self.fenetre.blit(img3, (72,0))
        elif n <= 0 :
            img1 = pygame.image.load("image/0 Timer.png").convert_alpha()
            self.fenetre.blit(img1, (0,0))
            img2 = pygame.image.load ("image/0 Timer.png").convert_alpha()
            self.fenetre.blit(img2, (36,0))
            img3 = pygame.image.load ("image/0 Timer.png").convert_alpha()
            self.fenetre.blit(img3, (72,0))


    def timer (self) :
        """
        fonction permettant de calculer le temps écoulé depuis le début de la partie.
        """
        global n,a
        self.t2 = time.time ()
        a = n - floor (self.t2 - self.t1)
        Perso.open_img(self,a)
        if a < 0 :
            Perso.victoire(self) # si le temps est écoulé la partie est gagné

    def idle(self):
        """
        fonction définissant les paramètres par défault du personnage
        """
        global nb_vie,difficulte

        self.frame=self.base
        self.fenetre.blit(self.fond,(0,0)) # on offiche le fond.
        ennemy_test.Ennemy.colli(self.x,self.y,self.dim) # on regarde les collision entre les ennemies et le personnage.
        ennemy_test.Ennemy.genEnnemy() # on génère les ennemies si besoin.
        Perso.updateEnnemy(self) # on afffiche les ennemies.
        self.fenetre.blit(self.frame,(self.x,self.y)) # on affiche le personnage.
        Perso.timer(self) # on affiche le timer.
        Perso.vie(self,nb_vie) # on affiche la vie.
        Perso.affScore(self) # on affiche le score.
        pygame.display.flip() # on rafraichît l'écran. // ce groupement d'instruction sera réutilisé tout le long du programme, une optimisation aurait donc été de créer une fonction.

    def updateEnnemy(self) :
        """
        fonction permettant l'affichage des ennemies.
        """
        re=pygame.image.load("image/ennemy.png")
        for ennemy in constantegagam.ennemy_list :
            self.fenetre.blit(re,(ennemy[0],ennemy[1]))

    def borders(self):
        """
        fonction délimitant les limites de la fenêtre.
        """
        if self.x<-70:
            self.x=-69
        elif self.x>990:
            self.x=989

    def gravity(self,grav,side):
        """
        fonction définissant la gravité.
        """
        global nb_vie,difficulte

        self.dim = 100

        if self.y<388:
            self.fallspd=floor(2.21*self.gtime*self.gtime)
            self.frame=self.j[side]
            self.y=self.y+self.fallspd
            self.x+=grav
            self.gtime=self.gtime+1/60
            self.onground=False
        if self.y>388:
            self.frame=self.base
            self.y=388
            self.gtime=0.9
            self.onground=True
        if self.y==388:
            self.onground=True
        Perso.borders(self)
        ennemy_test.Ennemy.move(self.x,self.y)
        self.fenetre.blit(self.fond,(0,0))
        ennemy_test.Ennemy.colli(self.x,self.y,self.dim)
        ennemy_test.Ennemy.genEnnemy()
        Perso.updateEnnemy(self)
        self.fenetre.blit(self.frame,(self.x,self.y))
        Perso.timer(self)
        Perso.vie(self,nb_vie)
        Perso.affScore(self)
        pygame.display.flip()
        return self.onground

    def gravity_no_frame(self,grav):
        """
        fonction définissant la gravité sans les frames.
        """
        if self.y<368:
            self.y=self.y+floor(2.21*self.gtime*self.gtime)
            self.x+=grav
            self.gtime=self.gtime+1/60
            self.onground=False
        if self.y>368:
            self.frame=self.base
            self.y=368
            self.gtime=0.9
            self.onground=True
        if self.y==368:
            self.onground=True

        Perso.borders(self)
        return self.onground

    def speed(self,dir):
        """
        fonction définissant la vitesse de déplacement du personnage
        """
        self.rawspd=floor(dir*self.speed)
        self.speed+=0.3

        if self.speed>5:
        	self.speed=5

        time.sleep(8/60-self.speed/60)
        return self.rawspd

    def move(self,dir):
        """
        fonction gérant les déplacements au sol du personnage.
        """
        global nb_vie,difficulte

        self.hit=0
        self.dim = 100

        if dir!=self.dirmem :
        	self.ani=0
        	self.speed=0.1

        self.dirmem=dir
        self.x+=Perso.speed(self,dir)

        if self.onground==True:
        	if dir<0:
        		self.frame=self.l[floor(self.ani/2)]
        		self.ani+=1

        		if self.ani>=24:
        			self.ani=0
        	else:
        		self.frame=self.r[floor(self.ani/2)]
        		self.ani+=1

        		if self.ani>=24:
        			self.ani=0

        elif self.onground==False:
        	self.frame=self.j[1]

        Perso.borders(self)
        ennemy_test.Ennemy.move(self.x,self.y)
        self.fenetre.blit(self.fond,(0,0))
        ennemy_test.Ennemy.colli(self.x,self.y,self.dim)
        ennemy_test.Ennemy.genEnnemy()
        Perso.updateEnnemy(self)
        self.fenetre.blit(self.frame,(self.x,self.y))
        Perso.timer(self)
        Perso.vie(self,nb_vie)
        Perso.affScore(self)
        pygame.display.flip()

    def jump(self,direc,side):
        """
        fonction gérant le saut du personnage.
        """
        global nb_vie,difficulte

        self.hit=0
        self.dim = 100

        if self.onground==True:
            self.yinit=self.y-182
            self.onground=False

            while (self.y>self.yinit):
                self.frame=self.j[side-1]
                self.x+=direc
                Perso.borders(self)
                self.y-=self.jumpspd
                Perso.gravity_no_frame(self,direc)
                ennemy_test.Ennemy.move(self.x,self.y)
                self.fenetre.blit(self.fond,(0,0))
                ennemy_test.Ennemy.colli(self.x,self.y,self.dim)
                ennemy_test.Ennemy.genEnnemy()
                Perso.updateEnnemy(self)
                self.fenetre.blit(self.frame,(self.x,self.y))
                Perso.timer(self)
                Perso.vie(self,nb_vie)
                Perso.affScore(self)
                pygame.display.flip()
                time.sleep(1/120)
            self.gtime=0.1

    def jump_pulse(self):
        """
        fonction gérant l'affichage de l'animation de saut.
        """
        if self.onground==True:
        	self.frame=self.j[0]

    def strike1(self,grav,side):
        """
        fonction gérant la première attaque du personnage.
        """
        global nb_vie,difficulte

        self.dim = 150

        if self.onground==True:
            for i in range (7):
                if side==1:
                    self.frame=self.s[i]

                elif side==3:
                    self.frame=self.sl[i]

                ennemy_test.Ennemy.move(self.x,self.y)
                self.fenetre.blit(self.fond,(0,0))
                ennemy_test.Ennemy.colli(self.x,self.y,self.dim)
                ennemy_test.Ennemy.genEnnemy()
                Perso.updateEnnemy(self)
                self.fenetre.blit(self.frame,(self.x,self.y-20))
                Perso.timer(self)
                Perso.vie(self,nb_vie)
                Perso.affScore(self)
                pygame.display.flip()
                time.sleep(3/60)
            Perso.idle(self)

    def strike2(self,grav,side):
        """
        fonction gérant la deuxième attaque du personnage.
        """

        global nb_vie,difficulte

        self.dim = 150

        if self.onground==True:
            for i in range (10):
                if side==1:
                    self.frame=self.s[i+7]

                elif side==3:
                    self.frame=self.sl[i+7]

                ennemy_test.Ennemy.move(self.x,self.y)
                self.fenetre.blit(self.fond,(0,0))
                ennemy_test.Ennemy.colli(self.x,self.y,self.dim)
                ennemy_test.Ennemy.genEnnemy()
                Perso.updateEnnemy(self)
                self.fenetre.blit(self.frame,(self.x,self.y-20-(i*7)))
                Perso.timer(self)
                Perso.vie(self,nb_vie)
                Perso.affScore(self)
                pygame.display.flip()
                time.sleep(2/60)
            Perso.idle(self)

    def airstrike(self,grav,side):
        """
        fonction gérant l'attaque aérienne du personnage.
        """
        global nb_vie,difficulte

        self.hit=0
        self.dim = 200
        for i in range (7):
            if self.onground==False:
                if side==1:
                    self.frame=self.airs[i+1]
                elif side==3:
                    self.frame=self.airsl[i+1]

                self.onground=Perso.gravity_no_frame(self,grav)
                ennemy_test.Ennemy.move(self.x,self.y)
                self.fenetre.blit(self.fond,(0,0))
                ennemy_test.Ennemy.colli(self.x,self.y,self.dim)
                ennemy_test.Ennemy.genEnnemy()
                Perso.updateEnnemy(self)
                self.fenetre.blit(self.frame,(self.x,self.y-50))
                Perso.timer(self)
                Perso.vie(self,nb_vie)
                Perso.affScore(self)
                pygame.display.flip()
                time.sleep(3/60)

    def combo(self,grav,side):
        """
        fonction gérant le combo du personnage (attaque 1 puis attaque 2).
        """
        self.hit+=1

        if self.hit>2:
            self.hit=1

        if self.onground==True:
            if self.hit==1:
                Perso.strike1(self,grav,side)
            elif self.hit==2:
                Perso.strike2(self,grav,side)

        elif self.onground==False:
            Perso.airstrike(self,grav,side)

    def victoire(self):
        """
        fonction affichant l'image de victoire.
        """
        global deft,vic
        if deft != True :
            win = pygame.image.load("image/v1.png").convert_alpha()
            self.fenetre.blit(win, (250,150))
            Perso.Score() # on enregistre le score si besoin.
            vic = True

    def vie(self,nb_vie):
        """
        fonction gérant l'affichage de la vie du personnage.
        """
        if nb_vie==3 :
            img_vie=pygame.image.load("image/imgVie.png").convert_alpha()
            self.fenetre.blit(img_vie,(930,10))
        elif nb_vie==2 :
            img_vie=pygame.image.load("image/imgVie1.png").convert_alpha()
            self.fenetre.blit(img_vie,(930,10))
        elif nb_vie==1 :
            img_vie=pygame.image.load("image/imgVie2.png").convert_alpha()
            self.fenetre.blit(img_vie,(930,10))
        elif nb_vie <= 0 :
            Perso.defaite(self)
            Perso.Score()

    def defaite(self) :
        """
        fonction gérant l'affichage de l'écran de défaite.
        """
        global deft,vic
        if vic != True :
            d=pygame.image.load("image/d.png").convert_alpha()
            self.fenetre.blit(d, (180,130))
            deft = True

    def affScore(self) :
        """
        fonction permettant d'afficher le score.
        """
        n=0
        pp=str(constantegagam.point)
        font = pygame.font.Font(None, 36)
        text = font.render("Score : ", 1, (10, 10, 10))
        text2 = font.render("Meilleur Score : "+constantegagam.Mscore, 1, (10, 10, 10))
        self.fenetre.blit(text,(400,10))
        self.fenetre.blit(text2,(400,60))
        for i in pp :
            sc = pygame.image.load("image/"+i+" timer score.png")
            self.fenetre.blit(sc,(500+n*36,0))
            n += 1

    def Score() :
        """
        fonction permettant d'enregistrer le meilleur score en fin de partie.
        """
        if int(constantegagam.point) > int(constantegagam.Mscore) : # si le score est supérieur au meilleur score ...
            score = open("score.txt","w")
            score.write(str(constantegagam.point)) # ... il devient le meilleur score.
            score.close()
