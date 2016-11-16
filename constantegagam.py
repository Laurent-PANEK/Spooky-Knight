#-*-coding:utf8-*-
"""
    on importe tous les modules nécessaires.
"""
import pygame
import pickle
from pygame.locals import*

pygame.display.init() # on initialise le module display.

# on définit les variables qui seront utilisé dans les différent fichiers.
dimensions=(1000,480)
fenetre=pygame.display.set_mode(dimensions,FULLSCREEN)
fond=pygame.image.load("image/spookyworld.png").convert()
title="Spooky Knight"
icon=pygame.image.load("image/sk.png").convert()
sheet=pygame.image.load("image/spookyrun.png").convert_alpha()
ground = 454
ennemy_number=0
ennemy_list=[]
x_y = []
point = 0
score = open("score.txt","r")
Mscore = score.read()
score.close()

#anims:
base=pygame.image.load("image/spookidle.png").convert_alpha()

#run anims:
#right
r1=pygame.image.load("image/spookyrun01.png").convert_alpha()
r2=pygame.image.load("image/spookyrun02.png").convert_alpha()
r3=pygame.image.load("image/spookyrun03.png").convert_alpha()
r4=pygame.image.load("image/spookyrun04.png").convert_alpha()
r5=pygame.image.load("image/spookyrun05.png").convert_alpha()
r6=pygame.image.load("image/spookyrun06.png").convert_alpha()
r7=pygame.image.load("image/spookyrun07.png").convert_alpha()
r8=pygame.image.load("image/spookyrun08.png").convert_alpha()
r9=pygame.image.load("image/spookyrun09.png").convert_alpha()
r10=pygame.image.load("image/spookyrun10.png").convert_alpha()
r11=pygame.image.load("image/spookyrun11.png").convert_alpha()
r12=pygame.image.load("image/spookyrun12.png").convert_alpha()
run_right=[r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12]

#left
l1=pygame.image.load("image/spookyrunl01.png").convert_alpha()
l2=pygame.image.load("image/spookyrunl02.png").convert_alpha()
l3=pygame.image.load("image/spookyrunl03.png").convert_alpha()
l4=pygame.image.load("image/spookyrunl04.png").convert_alpha()
l5=pygame.image.load("image/spookyrunl05.png").convert_alpha()
l6=pygame.image.load("image/spookyrunl06.png").convert_alpha()
l7=pygame.image.load("image/spookyrunl07.png").convert_alpha()
l8=pygame.image.load("image/spookyrunl08.png").convert_alpha()
l9=pygame.image.load("image/spookyrunl09.png").convert_alpha()
l10=pygame.image.load("image/spookyrunl10.png").convert_alpha()
l11=pygame.image.load("image/spookyrunl11.png").convert_alpha()
l12=pygame.image.load("image/spookyrunl12.png").convert_alpha()
run_left=[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12]

#strike right:
s1=pygame.image.load("image/spookystrike01.png").convert_alpha()
s2=pygame.image.load("image/spookystrike02.png").convert_alpha()
s3=pygame.image.load("image/spookystrike03.png").convert_alpha()
s4=pygame.image.load("image/spookystrike04.png").convert_alpha()
s5=pygame.image.load("image/spookystrike05.png").convert_alpha()
s6=pygame.image.load("image/spookystrike06.png").convert_alpha()
s7=pygame.image.load("image/spookystrike07.png").convert_alpha()

#strike2 right:
s_2_1=pygame.image.load("image/spookystrike21.png").convert_alpha()
s_2_2=pygame.image.load("image/spookystrike22.png").convert_alpha()
s_2_3=pygame.image.load("image/spookystrike23.png").convert_alpha()
s_2_4=pygame.image.load("image/spookystrike24.png").convert_alpha()
s_2_5=pygame.image.load("image/spookystrike25.png").convert_alpha()
s_2_6=pygame.image.load("image/spookystrike26.png").convert_alpha()
s_2_7=pygame.image.load("image/spookystrike27.png").convert_alpha()
s_2_8=pygame.image.load("image/spookystrike28.png").convert_alpha()
s_2_9=pygame.image.load("image/spookystrike29.png").convert_alpha()
s_2_10=pygame.image.load("image/spookystrike210.png").convert_alpha()

# strike left
sl1=pygame.image.load("image/spookystrikel01.png").convert_alpha()
sl2=pygame.image.load("image/spookystrikel02.png").convert_alpha()
sl3=pygame.image.load("image/spookystrikel03.png").convert_alpha()
sl4=pygame.image.load("image/spookystrikel04.png").convert_alpha()
sl5=pygame.image.load("image/spookystrikel05.png").convert_alpha()
sl6=pygame.image.load("image/spookystrikel06.png").convert_alpha()
sl7=pygame.image.load("image/spookystrikel07.png").convert_alpha()

#strike 2 left
sl_2_1=pygame.image.load("image/spookystrike2l1.png").convert_alpha()
sl_2_2=pygame.image.load("image/spookystrike2l2.png").convert_alpha()
sl_2_3=pygame.image.load("image/spookystrike2l3.png").convert_alpha()
sl_2_4=pygame.image.load("image/spookystrike2l4.png").convert_alpha()
sl_2_5=pygame.image.load("image/spookystrike2l5.png").convert_alpha()
sl_2_6=pygame.image.load("image/spookystrike2l6.png").convert_alpha()
sl_2_7=pygame.image.load("image/spookystrike2l7.png").convert_alpha()
sl_2_8=pygame.image.load("image/spookystrike2l8.png").convert_alpha()
sl_2_9=pygame.image.load("image/spookystrike2l9.png").convert_alpha()
sl_2_10=pygame.image.load("image/spookystrike2l10.png").convert_alpha()

strike_right=[s1,s2,s3,s4,s5,s6,s7,s_2_1,s_2_2,s_2_3,s_2_4,s_2_5,s_2_6,s_2_7,s_2_8,s_2_9,s_2_10]
strike_left=[sl1,sl2,sl3,sl4,sl5,sl6,sl7,sl_2_1,sl_2_2,sl_2_3,sl_2_4,sl_2_5,sl_2_6,sl_2_7,sl_2_8,sl_2_9,sl_2_10]

#airstrike :
#right
as1=pygame.image.load("image/spookyair01.png").convert_alpha()
as2=pygame.image.load("image/spookyair02.png").convert_alpha()
as3=pygame.image.load("image/spookyair03.png").convert_alpha()
as4=pygame.image.load("image/spookyair04.png").convert_alpha()
as5=pygame.image.load("image/spookyair05.png").convert_alpha()
as6=pygame.image.load("image/spookyair06.png").convert_alpha()
as7=pygame.image.load("image/spookyair07.png").convert_alpha()
as8=pygame.image.load("image/spookyair08.png").convert_alpha()
#left
asl1=pygame.image.load("image/spookyairl01.png").convert_alpha()
asl2=pygame.image.load("image/spookyairl02.png").convert_alpha()
asl3=pygame.image.load("image/spookyairl03.png").convert_alpha()
asl4=pygame.image.load("image/spookyairl04.png").convert_alpha()
asl5=pygame.image.load("image/spookyairl05.png").convert_alpha()
asl6=pygame.image.load("image/spookyairl06.png").convert_alpha()
asl7=pygame.image.load("image/spookyairl07.png").convert_alpha()
asl8=pygame.image.load("image/spookyairl08.png").convert_alpha()

airstrike_right=[as1,as2,as3,as4,as5,as6,as7,as8]
airstrike_left=[asl1,asl2,asl3,asl4,asl5,asl6,asl7,asl8]

actions=["move","jump","attack"]