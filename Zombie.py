#!/usr/bin/env python3
#Zombie.py
'''
all my comments/questions are docstrings that start w 'JS', so you can just 
cmd+F 'JS' and you'll find them

Changes:
- Renamed show func to draw
- Mostly didn't change anything, didn't want to fuck up pathfinding
'''
__author__ = "Ben Bloomgren and Jack Scheffel"
__version__ = "0.1.0"
__date__ = "2019.3.20"

from tkinter import Tk, Canvas
import math
import A_Star
from time import sleep
import random

def dist(self, other):
    # distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    d = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    return d


def random_probability(percent):
    epsilon = percent/100
    if random.random() < epsilon:
        return True
    else:
        return False

class Marker:
    def __init__(self, canvas, x, y, scale):
        self.canvas = canvas
        self.x = x * scale + (scale / 2)
        self.y = y * scale + (scale / 2)
        self.grid_x = (self.x - (scale / 2)) / scale
        self.grid_y = (self.y - (scale / 2)) / scale
        self.scale = scale

    def draw(self):
        self.canvas.create_oval(self.x - self.scale / 8,
                                self.y - self.scale / 8,
                                self.x + self.scale / 8,
                                self.y + self.scale / 8,
                                fill='red')


class Zombie:
    def __init__(self, canvas, parent, x, y, scale, pr=300):
        self.canvas = canvas
        self.x = x * scale + (scale / 2)
        self.y = y * scale + (scale / 2)
        self.grid_x = (self.x - (scale / 2)) / scale
        self.grid_y = (self.y - (scale / 2)) / scale
        self.pr = pr
        self.scale = scale
        self.r = self.scale / 4
        self.health = 100
        self.alive = True
        self.shape = None
        self.parent = parent

    def draw(self):
        if self.alive:
            self.shape = self.canvas.create_oval(self.x - self.scale / 4,
                                                 self.y - self.scale / 4,
                                                 self.x + self.scale / 4,
                                                 self.y + self.scale / 4)

    def seek_player_path(self, p, map):
        if dist(self, p) <= self.pr:
            start = (int(self.grid_x), int(self.grid_y))
            end = (int(p.grid_x), int(p.grid_y))
            print(start)
            print(end)
            path = A_Star.astar(map, start, end)
            print(path)
            for i in range(len(path)):
                m = Marker(self.canvas, path[i][0], path[i][1], self.scale)


# uses pathfinding to move towards player

    def seek_player(self, p, map, FRAME_COUNT):
        if FRAME_COUNT % 20 == 0:
            in_range = dist(self, p) <= self.pr
            if in_range:
                self.grid_x = (self.x - (self.scale / 2)) / self.scale
                self.grid_y = (self.y - (self.scale / 2)) / self.scale

                # p.grid_x = (p.x - (p.SCALE / 2)) / p.SCALE
                # p.grid_y = (p.y - (p.SCALE / 2)) / p.SCALE

                start = (int(self.grid_x), int(self.grid_y))
                end = (int(p.grid_x), int(p.grid_y))

                # print(start)
                # print(end)

                path = A_Star.astar(map, start, end)
                # print(path)

                self.move(path)

            else:
                pass

    def move(self, path):
        if len(path) > 1:
            new_pos = path[1]
            new_x = new_pos[0]
            new_y = new_pos[1]

            self.x = new_x * self.scale + (self.scale / 2)
            self.y = new_y * self.scale + (self.scale / 2)
        else:
            new_pos = path[0]
            new_x = new_pos[0]
            new_y = new_pos[1]

            self.x = new_x * self.scale + (self.scale / 2)
            self.y = new_y * self.scale + (self.scale / 2)

    def hurt(self, damage):
        is_dead = False
        self.health -= damage
        if self.health <= 0:
            is_dead = True
        if is_dead:
            return True
        return False

    def kill(self):
        self.alive = False
        self.canvas.delete(self.shape)
