#!/usr/bin/env python3
#Grid.py
'''
all my comments/questions are docstrings that start w 'JS', so you can just 
cmd+F 'JS' and you'll find them

Changes:
- Load map automatically
- optimize __init__ arguments
- always load map
    - this is now in the __init__ func
- renamed show func to draw
'''
__author__ = "Ben Bloomgren and Jack Scheffel"
__version__ = "0.1.0"
__date__ = "2019.3.20"

class Grid:
    def __init__(self, canvas, c_height, c_width, map):
        self.MAP_WIDTH = len(map[0])
        self.MAP_HEIGHT = len(map)
        self.C_WIDTH = c_width
        self.C_HEIGHT = c_height

        self.zombie_spawns = []
        self.player_spawn = None
        self.wall_coors = []
        self.SCALE = self.C_WIDTH / self.MAP_WIDTH
        self.canvas = canvas

        #automatically load map
        for i in range(self.MAP_HEIGHT):
            for j in range(self.MAP_WIDTH):
                if map[i][j] == 1:
                    self.wall_coors.append((i * self.SCALE + self.SCALE/2, j * self.SCALE + self.SCALE/2))
                if map[i][j] == 'z':
                    self.zombie_spawns.append((i, j))
                if map[i][j] == 'p':
                    self.player_spawn = (i, j)

    def draw(self):
        for i in range(self.MAP_WIDTH):
            self.canvas.create_line(i * self.SCALE, 0, i * self.SCALE, self.C_HEIGHT, fill="#000000")
        for i in range(self.MAP_HEIGHT):
            self.canvas.create_line(0, i * self.SCALE, self.C_WIDTH, i * self.SCALE, fill="#000000")

        for i in range(len(self.wall_coors)):
            self.canvas.create_rectangle(
                self.wall_coors[i][0] - self.SCALE/2,
                self.wall_coors[i][1] - self.SCALE/2,
                self.wall_coors[i][0] + self.SCALE/2,
                self.wall_coors[i][1] + self.SCALE/2,
                fill="#000000")

    def get_grid_info(self):
        return self.wall_coors, self.player_spawn
