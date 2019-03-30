import numpy as np
from tkinter import Tk, Canvas
import random

        #0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11
map_ = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
        [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],  # 2
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 3
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 4
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 7
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 8
        [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],  # 9
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # 11


def create_canvas(w=600, h=600, bg="black", title="Untitled"):
    global width, height
    width = w
    height = h
    root = Tk()
    root.title(title)
    canvas = Canvas(root, height=height, width=width, bg=bg)
    canvas.pack()
    return root, canvas


def random_probability(percent):
    epsilon = percent/100
    if random.random() < epsilon:
        return True
    else:
        return False


def generate(w, h):
    p = 2
    z = 3
    map = [[0 for _ in range(w)]for _ in range(h)]
    # map = np.zeros([w, h])
    for x in range(w):
        for y in range(h):
            # if random_probability(20):
            #     map[x][y] = 1

            if x == 0 or x == w - 1 or y == 0 or y == h - 1:
                map[y][x] = 1

            if x == 1 and y == 1:
                map[y][x] = p

            if (x % 3 == 0 and y % 3 == 0) and map[y][x] == 0:
                map[y][x] = z

    place(house, map, 15, 10)

    # for i in range(w):
    #     print(map[i])

    return map

###############################
# Randomly occurring structures
###############################

block = [[1, 1, 1, 1],
         [1, 0, 0, 1]]

house = [[1, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1],
         [1, 0, 1, 1, 0, 1]]



def place(structure, map, x, y):

    x_len = len(structure)
    y_len = len(structure[0])

    for i in range(x_len):
        for j in range(y_len):
            try:
                if structure[i][j] == 1:
                    map[y+j][x+i] = 1
            except IndexError:
                print(f"I: {i}\nJ:{j}")

class Button:
    def __init__(self, canvas, x, y, w):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.w = w
        self.shape = None
        self.color = 'pink'
        self.state = False

    def draw(self):
        if self.state:
            self.color = 'blue'
        else:
            self.color = 'pink'

        if self.shape is not None:
            self.canvas.delete(self.shape)
        self.shape = self.canvas.create_rectangle(self.x - self.w/2,
                                                  self.y - self.w/2,
                                                  self.x + self.w/2,
                                                  self.y + self.w/2,
                                                  fill=self.color,
                                                  activefill= "green")

    def switch(self):
        if self.state:
            self.state = False
        else:
            self.state = True

    def clicked(self, mousex, mousey):
        x = range(int(self.x - self.w / 2), int(self.x + self.w / 2))
        y = range(int(self.y - self.w / 2), int(self.y + self.w / 2))
        if mousex in x and mousey in y:

            self.color='blue'
            return True
        else:
            return False


class MapEditor:
    def __init__(self, w, h, map_width, map_height, map=None):
        self.root, self.canvas = create_canvas(w, h, "white", "Map Editor")
        self.C_WIDTH = w
        self.C_HEIGHT = h
        self.SCALE = w / map_width
        self.map = map
        self.M_WIDTH = map_width
        self.M_HEIGHT = map_height
        self.squares = []
        self.create_squares()
        if map is None:
            self.create_map()
        else:
            self.load_map()

    def create_map(self):
        self.map = [[0 for _ in range(self.M_WIDTH)]for _ in range(self.M_HEIGHT)]

    def load_map(self):
        for i in range(self.M_WIDTH):
            for j in range(self.M_HEIGHT):
                if self.map[i][j] == 1:
                    self.squares[i][j].state = True

    def show_grid(self):    # unused at the moment
        for i in range(self.M_WIDTH):
            self.canvas.create_line(i * self.SCALE, 0, i * self.SCALE, self.C_HEIGHT, fill="#000000")
        for i in range(self.M_HEIGHT):
            self.canvas.create_line(0, i * self.SCALE, self.C_WIDTH, i * self.SCALE, fill="#000000")

    def create_squares(self):
        self.squares = [[Button(self.canvas, i * self.SCALE + self.SCALE/2, j * self.SCALE + self.SCALE/2, self.SCALE)
                         for i in range(self.M_WIDTH)] for j in range(self.M_HEIGHT)]

    def show(self):
        for rows in self.squares:
            for square in rows:
                square.draw()




def mouse_clicked(event):
    for i, rows in enumerate(e.squares):
        for j, square in enumerate(rows):
            if square.clicked(event.x, event.y):
                square.switch()
                if square.state:
                    e.map[i][j] = 1
                else:
                    e.map[i][j] = 0
                print(f"I: {i}\tJ: {j}")


def preview_map(event):
    print('\n\nMAP PREVIEW:')
    for row in e.map:
        print(row)


def clear_map(event):
    for i, rows in enumerate(e.squares):
        for j, square in enumerate(rows):
            e.squares[i][j].state = False
            e.map[i][j] = 0


if __name__ == '__main__':
    e = MapEditor(600, 600, 12 ,12) # you can also load up a map to edit
    e.root.bind("<Button-1>", mouse_clicked)
    e.root.bind("<space>", preview_map)
    e.root.bind("<Shift-BackSpace>", clear_map)

    while True:
        e.show()
        e.canvas.update()
