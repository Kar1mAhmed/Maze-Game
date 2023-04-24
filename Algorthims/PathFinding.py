from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

matrix = [
    [1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 1]]

grid = Grid(matrix=matrix)

start = grid.node(0, 0)
end = grid.node(6, 3)
 
finder = AStarFinder(diagonal_movement=DiagonalMovement.always)

path, run = finder.find_path(start, end, grid)

print(path)
