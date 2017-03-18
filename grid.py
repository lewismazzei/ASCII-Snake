from cell import Cell

class Grid():
	def __init__(self, state = [[Cell() for col in range(10)] for row in range(10)]):
		self.state = state

	def __str__(self):
		return '{}'.format([print([print('|', str(self.state[row][col]), end = '|') for col in range(5)]) for row in range(5)])

grid = Grid()

print(grid)