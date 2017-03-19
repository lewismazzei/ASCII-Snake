from cell import Cell
from snake import Snake

class Grid():
	def __init__(self, state = [[Cell(location = (row, col)) for col in range(10)] for row in range(10)]):
		self.state = state

	def __str__(self):
		output = ''
		for row in range(10):
			for col in range(10):
				output += str(self.state[row][col])
			output += "\n"
		return output

	def updateHead(self, snake):
		self.state[snake.headPos[0]][snake.headPos[1]].char = '@'
