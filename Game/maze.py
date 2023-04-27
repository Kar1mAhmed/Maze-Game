from Game.maze_creator import maze

rows = 20
cols = 10

my_maze = maze(rows=rows, cols=cols)
my_maze.CreateMaze()


#my_maze.run()


Map = my_maze.maze_map
#print(Map)
# for i in range(1,11):
#     Map[(1, i)]['E'] = 0
#     Map[(10, i)]['E'] = 0


# for key in Map.keys():
#     Map[key] = {'W' : 1, 'N' : 1, 'E' : 1, 'S' : 1}

# Map[(1,1)] = {'W' : 0, 'N' : 0, 'E' : 0, 'S' : 1}
# Map[(1,2)] = {'W' : 0, 'N' : 1, 'E' : 0, 'S' : 1}
# Map[(1,3)] = {'W' : 0, 'N' : 1, 'E' : 1, 'S' : 1}
# Map[(1,3)] = {'W' : 0, 'N' : 1, 'E' : 1, 'S' : 1}





# Map = []

# # build empty map
# for x in range(rows * 2 ):
#     row = []
#     for y in range(cols * 2 ):
#         if y == 0 or y == (cols * 2) - 1:
#             row.append('H')
#         elif x == 0 or x == (rows * 2) - 1:
#             row.append('V')
#         else:
#             row.append('.')
#     Map.append(row)

# for x in range(rows):
#     for y in range(cols):
#         cell = my_maze.maze_map[(x + 1, y + 1)]
#         for key, value in cell.items():
#             _x = x * 2
#             _y = y * 2
#             if key == 'N' and value == 0:
#                 Map[_x][_y - 1] = 'V'
#             if key == 'W' and value == 0:
#                 Map[_x-1][_y] = 'H'
#             if key == 'E' and value == 0:
#                 Map[_x+1][_y] = 'H'
#             if key == 'S' and value == 0:
#                 Map[_x][_y+1] = 'V'
# Map[1][1] = 'P'
