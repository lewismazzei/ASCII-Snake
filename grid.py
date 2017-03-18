from cell import Cell
from snake import Snake

class Grid():
	def __init__(self, state = [[Cell(location = (row, col)) for col in range(10)] for row in range(10)]):
		self.state = state

	def __str__(self):
		return '{}'.format([print([print(str(self.state[row][col]), end = '') for col in range(10)]) for row in range(10)])

	def updateHead(self, snake):
		self.state[snake.headPos[0]][snake.headPos[1]].char = '@'

	'''def head(row, col)
	for row in grid.state:
		for col in row:
			if col.location == (row, col):
				col.char = '@'
				print(col)'''

