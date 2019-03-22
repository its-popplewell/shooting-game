#!/usr/bin/env python3
#Bullet.py
'''
all my comments/questions are docstrings that start w 'JS', so you can just 
cmd+F 'JS' and you'll find them

Changes:
- gave this its own file
- changed shooting, so shooting is no longer from player class
- bullet color now black
'''
__author__ = "Ben Bloomgren and Jack Scheffel"
__version__ = "0.1.0"
__date__ = "2019.3.20"

import math

class Bullet:
    def __init__(self, canvas, x, y, x_going_to, y_going_to):
        self.canvas = canvas
        self.draw_x = x
        self.draw_y = y
        self.starting_x = x
        self.starting_y = y
        self.r = 2
        self.damage = 10
        
        self.angle = math.atan2(-(y - y_going_to), -(x - x_going_to))

        bullet_speed = 20
        self.dx = bullet_speed * math.cos(self.angle)
        self.dy = bullet_speed * math.sin(self.angle)
        
    def update(self):
        self.draw_x += self.dx
        self.draw_y += self.dy

    def draw(self):
        self.canvas.create_oval(
            self.draw_x - self.r, 
            self.draw_y - self.r, 
            self.draw_x + self.r, 
            self.draw_y + self.r, 
            fill="#000000")