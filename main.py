#!/usr/bin/env python3
#main.py
'''
all my comments/questions are docstrings that start w 'JS', so you can just
cmd+F 'JS' and you'll find them

Changes:
- Renamed some functions so everything was the same (show = draw, draw = draw)
- made Map var only initialized in main and passed into other objects
- using a after loop
- made bullet file
- added some commenting
- changed player movement -> words the same, just works a little better
    with the after loop
- Changed the shooting mechanism -> shooting is no longer a player function, but a
    function in main that runs on when mouse is clicked

Notes:
- try to use mostly hex for colors
'''
__author__ = "Ben Bloomgren and Jack Scheffel"
__version__ = "0.1.0"
__date__ = "2019.3.20"

from tkinter import Tk, Canvas
import random
from time import sleep
import math
from Zombie import Zombie
from Player import Player
from Grid import Grid
from Bullet import Bullet
import os

os.system('defaults write -g ApplePressAndHoldEnabled -bool false')  #for key repeating

###########
# Globals #
###########

p = 'p'
z = 'z'

        #0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11
map  = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
        [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],  # 2
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 3
        [0, 0, 1, 0, z, 0, 0, 0, 0, 1, 0, 0],  # 4
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 7
        [0, 0, 1, 0, 0, 0, 0, 0, p, 1, 0, 0],  # 8
        [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],  # 9
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # 11

bullets = []
zombies = []

C_HEIGHT = 480
C_WIDTH = 480
SCALE = C_WIDTH / len(map)
FRAME_COUNT = 0

####################################################################################

#############
# Functions #
#############

#create canvas and root object
def create_canvas(w=600, h=600, bg="black", title="Untitled"):
    global width, height
    width = w
    height = h
    root = Tk()
    root.title(title)
    canvas = Canvas(root, height=height, width=width, bg=bg)
    canvas.pack()
    return root, canvas

#when a key pressed, move player
def key_pressed(event):
    p.move(event.keysym, wall_coors)

#for the targeting line
def mouse_moved(event):
    p.target_x = event.x
    p.target_y = event.y

#for shooting
def mouse_clicked(event):
    b = Bullet(canvas, p.x, p.y, p.target_x, p.target_y)  #create new bullet
    bullets.append(b)  #append to bullet list

####################################################################################

#############
# Draw Loop #
#############

#coninuous loop
def loop():
    global FRAME_COUNT
    canvas.delete("all")  #clear canvas each time
    g.draw()
    p.draw()

    #check collisions on bullets
    if len(bullets) >= 1:
        bullet_it = 0
        while bullet_it < len(bullets):
            b = bullets[bullet_it]

            #check to see if bullets hit walls
            for w in wall_coors:
                if abs(b.draw_x - w[0]) < SCALE/2 and abs(b.draw_y - w[1]) < SCALE/2:
                    del bullets[bullet_it]
                    break

            #check to see if bullets hit zombies
            for z in zombies:
                if abs(b.draw_x - z.x) < SCALE/2 and abs(b.draw_y - z.y) < SCALE/2:
                    del bullets[bullet_it]
                    zombie_died = z.hurt(b.damage)
                    if zombie_died:
                        del zombies[zombies.index(z)]
                    break


            bullet_it += 1

    #draw all the bullets
    if len(bullets) >= 1:
        for b in bullets:
            b.update()
            b.draw()

    for z in zombies:
        # z.take_damage()
        z.seek_player(p, map, FRAME_COUNT)
        z.draw()

    FRAME_COUNT += 1

    root.after(17, loop)  #make loop continuous

####################################################################################

##########
# Set Up #
##########
if __name__ == "__main__":
    #create canvas
    root, canvas = create_canvas(C_WIDTH, C_HEIGHT, bg="white", title="Zombie Survival")
    root.focus_set()
    '''JS What does this(above) do?'''

    g = Grid(canvas, C_HEIGHT, C_WIDTH, map)  #create grid
    wall_coors, player_spawn = g.get_grid_info()  #get all important stuff from grid class

    p = Player(player_spawn[0], player_spawn[1], canvas, SCALE)  #make the player

    #make the zombies
    for i in range(len(g.zombie_spawns)):
        zombies.append(Zombie(canvas, g, g.zombie_spawns[i][0], g.zombie_spawns[i][1], SCALE))

    #bindings
    root.bind("<Key>", key_pressed)
    root.bind("<Motion>", mouse_moved)
    root.bind("<Button-1>", mouse_clicked)

    loop()

####################################################################################

#######
# Run #
#######

#run the app and turn back on the accent thing
root.mainloop()
os.system('defaults write -g ApplePressAndHoldEnabled -bool true')

####################################################################################



























# if __name__ == '__!main__':
#     root, canvas = create_canvas(480, 480, bg="white", title="Zombie Survival")
#     root.focus_set()
#     g = Grid(canvas, 12, 12, 480, 480)
#     g.load_map(map)
#     g.draw()

#     p = Player(canvas, g, g.player_spawn[0][0], g.player_spawn[0][1], g.scale, )
#     for i in range(len(g.zombie_spawns)):
#         g.zombies.append(Zombie(canvas, g, g.zombie_spawns[i][0], g.zombie_spawns[i][1], g.scale))

#     root.bind("<Key>", p.key_pressed)
#     root.bind("<Button-1>", p.shoot)

#     # beginning of loop

#     while True:

#         x = root.winfo_pointerx() - root.winfo_rootx()
#         y = root.winfo_pointery() - root.winfo_rooty()

#         p.update_crosshair(x, y)
#         p.show()

#         if len(g.bullets) >= 1:
#             bullet_it = 0
#             while bullet_it < len(g.bullets):
#                 b = g.bullets[bullet_it]
#                 for w in g.wall_coors:
#                     if abs(b.x - w[0]) < g.scale/2 and abs(b.y - w[1]) < g.scale/2:
#                         # print("HIT")
#                         del g.bullets[bullet_it]
#                         canvas.delete(b.shape)
#                         break

#                 for z in g.zombies:
#                     if abs(b.x - z.x) < g.scale/2 and abs(b.y - z.y) < g.scale/2:
#                         # print("HIT")
#                         del g.bullets[bullet_it]
#                         canvas.delete(b.shape)
#                         z.hurt(b.damage)
#                         break


#                 bullet_it += 1

#         if len(g.bullets) >= 1:
#             for b in g.bullets:
#                 b.update()
#                 b.show()

#         for z in g.zombies:
#             z.take_damage()
#             z.seek_player(p, map)
#             z.show()
#         canvas.update()
#         sleep(.1)
