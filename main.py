from grid import Grid
from cell import Cell
from snake import Snake

grid = Grid()
snake = Snake(((int(len(grid.state) / 2)), int(len(grid.state) / 2)))
grid.updateHead(snake)

print(grid)