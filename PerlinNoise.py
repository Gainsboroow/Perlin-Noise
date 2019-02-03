"""
Perlin Noise
Made by Gainsboroow 
Github : https://github.com/Gainsboroow/
Github repository : https://github.com/Gainsboroow/Perlin-Noise
"""

from random import *
import pygame
from pygame.locals import *

pygame.init()
size = width, height = 400, 400
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Perlin Noise")

caseSize = 50

vectorList = [ (-1,-1), (-1,1), (1,-1), (1,1) ] + [ (0,1), (0,-1), (-1,0), (1,0) ]
grid = [ [choice(vectorList) for i in range(width // caseSize + 2)] for a in range(height // caseSize + 2) ]

delta = [(0,0), (1,0), (0,1), (1,1)]

fade = lambda t :  t * t * t * (t * (t * 6 - 15) + 10)

for y in range(height):
    for x in range(width):
        caseX, caseY = x // caseSize, y // caseSize
        cornerVect = [ grid[caseY + dy][caseX + dx] for dx, dy in delta]
        distVect = [ (x/caseSize - caseX - dx, y/caseSize - caseY - dy) for dx, dy in delta]
        
        dotProd = [ cornerVect[i][0] * distVect[i][0] + cornerVect[i][1] * distVect[i][1] for i in range(4)]
        
        weightX, weightY = fade(x/caseSize - caseX), fade(y/caseSize - caseY)
        upperPoint = dotProd[0]*(1 - weightX) + dotProd[1]*(weightX)
        bottomPoint = dotProd[2]*(1 - weightX) + dotProd[3]*(weightX)


        final = upperPoint * (1 - weightY) + bottomPoint * (weightY)
        final *= 127
        final += 127
        
        pygame.draw.line(screen, (final, final, final), (x,y), (x,y) )

pygame.display.flip()
while 1:
    for event in pygame.event.get():
        if event.type == QUIT: 
                exit()    