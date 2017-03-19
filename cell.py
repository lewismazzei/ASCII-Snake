class Cell():
	def __init__(self, location, char = '#', lit = False):
		self.location = location
		self.char = char
		self.lit = lit

	#def __str__(self):
	#	return '{}:{}:{}'.format(self.char, self.lit, self.location)

	def __str__(self):
		return '{} '.format(self.char)
