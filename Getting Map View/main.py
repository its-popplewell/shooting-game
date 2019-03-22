H = 'p'

map  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, H, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

wanted_view_size = 5  #how wide you want the player to be - MUST BE ODD NUM >= 3
x = 6  #player x
y = 6  #player y

view_diff = int((wanted_view_size - 1) / 2)  #the num of cells on each side of the player

view_map = []  #this will become the view window

#for the y with the player centered
for i in range(y - view_diff, y + view_diff + 1):
    row = []
    #for the x with the player centered
    for j in range(x - view_diff, x + view_diff + 1):
        row.append(map[i][j])

    view_map.append(row)

# for rows in view_map:
#     print(rows)
