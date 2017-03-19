from grid import Grid
from cell import Cell
from snake import Snake
from math import floor
from time import sleep

grid = Grid()
snake = Snake(((floor(len(grid.state) / 2)), floor(len(grid.state) / 2)))
grid.updateHead(snake)

running = True
while running:
	sleep(1)
	

print('	<Word Here>\n')
print(grid)