# 1
import pygame
from pygame.locals import *
import math
import random

# 2
pygame.init()
width, height = 800, 500
screen=pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos=[150,100]
acc=[0,0]
arrows=[]
badtimer=100
badtimer1=0
badguys=[[640,100]]
healthvalue=194



# 3
player = pygame.image.load("/home/po/Desktop/github-projects/CTYI-Project-Po-/DudeR.png")
player = pygame.transform.scale(player, (300, 300))
grass = pygame.image.load("/home/po/Desktop/BB_Resources/resources/images/grass.png")
castle = pygame.image.load("/home/po/Desktop/github-projects/CTYI-Project-Po-/Base.png")
castle = pygame.transform.scale(castle, (100, 100))
arrow = pygame.image.load("/home/po/Desktop/BB_Resources/resources/images/bullet.png")
badguyimg1 = pygame.image.load("/home/po/Desktop/github-projects/CTYI-Project-Po-/Zombie.png")
badguyimg=badguyimg1
# 4
while 1:
    # 5
    screen.fill(0)
    # 6
    for x in range(width/grass.get_width()+1):
        for y in range(height/grass.get_height()+1):
            screen.blit(grass,(x*100,y*100))
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345 ))
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]),position[0]-(playerpos[0]))
    playerrot = pygame.transform.rotate(player, 1-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1) 
    for bullet in arrows:
        index=0
        velx=math.cos(bullet[0])*10
        vely=math.sin(bullet[0])*10
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        index+=1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))
            if badtimer==0:
             badguys.append([640, random.randint(50,430)])
            badtimer=100-(badtimer1*2)
        if badtimer1>=35:
            badtimer1=35
        else:
            badtimer1+=5
    index=0
    for badguy in badguys:
        if badguy[0]<-64:
            badguys.pop(index)
        badguy[0]-=7
        index+=1
    for badguy in badguys:
        screen.blit(badguyimg, badguy)
    # 7
    pygame.display.flip()
    # 8
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            acc[1]+=1
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])
    # 9
    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5
quit(0)
          

