'''
Created on 23-Jun-2020

@author: Toshinee Bhasin
'''
import pygame
from pygame.locals import *
import sys
import os
from pyrect import AREA
import random

#define display surface
Width,Height = 300, 525
half_width,half_height = Width/2 ,Height/2
AREA = Width * Height

#setup pygame
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Flappy Bird")
FPS = 120

background = pygame.image.load('D:/Flappy Bird/gallery/sprites/backgroundtry.png').convert()
x=0

#base
global basex,basex_change
baseImg = pygame.image.load('D:/Flappy Bird/gallery/sprites/basetry.png').convert_alpha()
basex = 0
basey = 380
basex_change = 0
GROUNDY = Height * 0.8

PIPE = 'D:/Flappy Bird/gallery/sprites/pipe.png'

pygame.init()
def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit() 
            
#os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"
#main loop

while True:
    events()
    
    rel_x = x % background.get_rect().width 
    print(background.get_rect().width )
    #print(rel_x)
    screen.blit(background,(rel_x - background.get_rect().width,0))
    if rel_x < Width:
        screen.blit(background,(rel_x,0))
    
    x -= 2
    #print(event)
    #pygame.draw.lines(DS,(255,0,0),(rel_x,0),(rel_x,Height),3)
    
    
    rel_base = basex % baseImg.get_rect().width
    screen.blit(baseImg,(rel_base - baseImg.get_rect().width,basey))
    if rel_base <Width:
        screen.blit(baseImg,(rel_base,basey))
        
    basex  -= 5
    
   
    pygame.display.update()
    CLOCK.tick(FPS)