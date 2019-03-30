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
        self.canvas = canvas  #canvas to draw obj on
        self.draw_x = x  #dynamic x val of bullet
        self.draw_y = y  #dynamic y val of bullet
        self.starting_x = x  #starting x pos of bullet to calc trajectory
        self.starting_y = y  #starting x pos of bullet to calc trajectory
        self.r = 2  #radius of bullet
        self.damage = 10  #damage amount of bullet

        self.angle = math.atan2(-(y - y_going_to), -(x - x_going_to))  #angle of trajectory of bullet

        bullet_speed = 20
        self.dx = bullet_speed * math.cos(self.angle)  #x change
        self.dy = bullet_speed * math.sin(self.angle)  #y change

    #update x and y
    def update(self):
        self.draw_x += self.dx
        self.draw_y += self.dy

    #draw the bullet on the canvas
    def draw(self):
        self.canvas.create_oval(
            self.draw_x - self.r,
            self.draw_y - self.r,
            self.draw_x + self.r,
            self.draw_y + self.r,
            fill="#000000")
