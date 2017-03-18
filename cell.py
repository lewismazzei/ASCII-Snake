class Cell():
	def __init__(self, char = '+', lit = False):
		self.char = char
		self.lit = lit

	def __str__(self):
		return '{}:{}'.format(self.char, self.lit)

cell = Cell()

print(str(cell))


