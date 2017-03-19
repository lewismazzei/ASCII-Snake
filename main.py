from math import floor
from time import sleep
import curses, random

LETTERS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

edgeCoords = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9),
		      (1, 0), (1, 9), (2, 0), (2, 9), (3, 0), (3, 9), (4, 0), (4, 9), (5, 0), (5, 9), 
		      (6, 0), (6, 9), (7, 0), (7, 9), (8, 0), (8, 9), (9, 0), (9, 1), (9, 2), (9, 3), 
		      (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9)]

shift = -5	
letterCount = -1
word = list(input('Select word: '))
nextLetter = word[letterCount + 1]

class Cell():
	def __init__(self, location):
		self.location = location
		if self.location not in edgeCoords:
			self.char = ' '
		else:
			self.char = '~'

	def __str__(self):
		return '{} '.format(self.char)

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

	def findNextCell(self, snake):
		if snake.direction == 'left':
			nextCell = self.state[snake.headPos[0]][snake.headPos[1] - 1]
			self.state[snake.headPos[0]][snake.headPos[1]].char = ' '
			snake.headPos = nextCell.location
			self.state[snake.headPos[0]][snake.headPos[1]].char = '@'
		elif snake.direction == 'right':
			nextCell = self.state[snake.headPos[0]][snake.headPos[1] + 1]
			self.state[snake.headPos[0]][snake.headPos[1]].char = ' '
			snake.headPos = nextCell.location
			self.state[snake.headPos[0]][snake.headPos[1]].char = '@'
		elif snake.direction == 'up':
			nextCell = self.state[snake.headPos[0] - 1][snake.headPos[1]]
			self.state[snake.headPos[0]][snake.headPos[1]].char = ' '
			snake.headPos = nextCell.location
			self.state[snake.headPos[0]][snake.headPos[1]].char = '@'
		elif snake.direction == 'down':
			nextCell = self.state[snake.headPos[0] + 1][snake.headPos[1]]
			self.state[snake.headPos[0]][snake.headPos[1]].char = ' '
			snake.headPos = nextCell.location
			self.state[snake.headPos[0]][snake.headPos[1]].char = '@'
		return nextCell

	def reset(self, grid):
		for row in range(10):
			for col in range(10):
				if grid.state[row][col].location not in edgeCoords:
					grid.state[row][col].char = ' '
				else:
					grid.state[row][col].char = '~'

	def spawnChars(self, grid):
		self.reset(grid)
		valid = False
		while not valid:
			char1Cell = random.choice(random.choice(grid.state))
			if char1Cell.location not in edgeCoords:
				valid = True
		valid = False
		while not valid:
			char2Cell = random.choice(random.choice(grid.state))
			if char2Cell.location not in edgeCoords:
				valid = True
		valid = False
		while not valid:
			char3Cell = random.choice(random.choice(grid.state))
			if char3Cell.location not in edgeCoords:
				valid = True
		valid = False
		while not valid:
			char4Cell = random.choice(random.choice(grid.state))
			if char4Cell.location not in edgeCoords:
				valid = True

		letters = []
		for i in range(3):
			letters.append(random.choice(LETTERS))	

		grid.state[char1Cell.location[0]][char1Cell.location[1]].char = word[letterCount + 1]
		grid.state[char2Cell.location[0]][char2Cell.location[1]].char = letters[0]
		grid.state[char3Cell.location[0]][char3Cell.location[1]].char = letters[1]
		grid.state[char4Cell.location[0]][char4Cell.location[1]].char = letters[2]


class Snake():
	def __init__(self, body = [], headPos = (4, 4), direction = 'left'):
		self.headPos = headPos
		self.direction = direction 
		self.body = body

grid = Grid()
snake = Snake()

def newLetters(grid):
	grid.spawnChars(grid)
	grid.state[snake.headPos[0]][snake.headPos[0]].char = '@'

newLetters(grid)


def main(stdscr, grid):
	stdscr = curses.initscr()
	curses.echo()
	stdscr.nodelay(1)
	running = True
	while running:
		event = stdscr.getch()
		if event == 260 and snake.direction != 'right':
			snake.direction = 'left'
		elif event == 261 and snake.direction != 'left':
			snake.direction = 'right'
		elif event == 259 and snake.direction != 'down':
			snake.direction = 'up'
		elif event == 258 and snake.direction != 'up':
			snake.direction = 'down'

				
		nextCell = grid.findNextCell(snake)
		if nextCell.location in edgeCoords:
			stdscr.clear()
			stdscr.addstr(0,0,'GAME OVER')
			stdscr.refresh()
			sleep(3)
			quit()
		elif nextCell.char == nextLetter:
			shift += 5
			snake.body.append(nextLetter)
			stdscr.addstr(0,0 + shift,'{}'.format(nextLetter))
			letterCount += 1
			newLetters(grid)
			stdscr.addstr(0,0,'\n\n{}'.format(grid))
			stdscr.refresh()

		stdscr.addstr(0,0,'\n\n{}'.format(grid))
		stdscr.refresh()
		sleep(0.5)


curses.wrapper(main, grid)