import pygame
import random
import colorsys
from pygame.locals import *

pygame.init()

master = pygame.display.set_mode((1000,500))
pygame.display.set_caption('Continous Ball')
clock = pygame.time.Clock()

color_list = [r, g, b]
h = 0

class Ball:
    def __init__(self):
        self.x = 500
        self.y = 250
        self.x_add = 3
        self.y_add = -1
        self.dirx = 1
        self.diry = 1
            
    def move(self, color):
        self.color = color
        
        if (self.x >= 965):
            self.dirx = self.dirx * (-1)
        if (self.x <= 35):
            self.dirx = self.dirx * (-1)
        if (self.y <= 35):
            self.diry = self.diry * (-1)
        if (self.y >= 465):
            self.diry = self.diry * (-1)
            
        self.x = self.x + (self.dirx * self.x_add)
        self.y = self.y + (self.diry * self.y_add)
        ball = pygame.draw.circle(master, self.color, (self.x, self.y), 35, 0)
        
ball = Ball()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if (h >= 1):
        h = 0
    h = h + 0.0015
    r, g, b = colorsys.hsv_to_rgb(h, 1, 1)
    color_rgb = [r, g, b]
    
    for color in range (0, 3):
        color_list[color] = int(round((color_rgb[color] * 255), 0))
    color = (color_list[0], color_list[1], color_list[2])
            
    master.fill(black)            
    ball.move(color)
            
    pygame.display.flip()
    clock.tick(30)
