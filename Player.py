#!/usr/bin/env python3
#Player.py
'''
all my comments/questions are docstrings that start w 'JS', so you can just 
cmd+F 'JS' and you'll find them

Changes:
- changed movement to run better with after loop in main
- optomized __init__ arguments
- show func now renamed to draw
'''
__author__ = "Ben Bloomgren and Jack Scheffel"
__version__ = "0.1.0"
__date__ = "2019.3.20"

from tkinter import Tk, Canvas
import math

class Player:
    def __init__(self, x, y, canvas, scale):
        self.x = (x * scale) + (scale / 2)
        self.y = (y * scale) + (scale / 2)
        self.grid_x = x
        self.grid_y = y
        self.SCALE = scale
        self.canvas = canvas
        self.health = None
        self.target_x = self.x  #for the targeting line
        self.target_y = self.y  #for the targeting line

    #draw the oval and the targeting line
    def draw(self):
        self.canvas.create_oval(
            self.x - self.SCALE / 4,
            self.y - self.SCALE / 4,
            self.x + self.SCALE / 4,
            self.y + self.SCALE / 4,
            fill="blue"
        )

        self.canvas.create_line(self.x, self.y, self.target_x, self.target_y)

    def move(self, move_direction, walls):
        x_change = 0
        y_change = 0

        if move_direction == 'w':
            x_change = 0
            y_change = -1 * self.SCALE
        elif move_direction == 'd':
            x_change = self.SCALE
            y_change = 0
        elif move_direction == 's':
            x_change = 0
            y_change = self.SCALE
        elif move_direction == 'a':
            x_change = -1 * self.SCALE
            y_change = 0

        self.x += x_change
        self.y += y_change


        #so you don't run off screen
        dont_loop = False
        if (self.x < 0 or self.x > self.canvas.winfo_width()) or (self.y < 0 or self.y > self.canvas.winfo_height()):
            self.x -= x_change
            self.y -= y_change
            dont_loop = True

        #so you don't move through walls
        for wall_loc in walls:
            if dont_loop:
                break
            if wall_loc[0] == self.x and wall_loc[1] == self.y:
                self.x -= x_change
                self.y -= y_change
                break
        
    