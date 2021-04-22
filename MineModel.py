import random

class MineModel:
	def __init__(self):
		# Start a new game
		self.newGame()

	# Starts a new game
	def newGame(self):
		# Holds number of rows and cols
		rows = 10
		cols = 10
		# Each button's contents is set 0
		self.grid = [[0]*(cols) for i in range(rows)]
		# Counts number of bombs added to the board
		bombNum = 0
		# Stores bombs adjacent to current button
		adj = 0

		# Adds 10 bombs to random buttons
		while bombNum != 10:
			# A random location for one bomb:
			i = random.randint(0, rows-1)
			j = random.randint(0, cols-1)
			# If there's not already a bomb in that spot, add it
			if self.grid[i][j] != 'X':
				self.grid[i][j] = 'X'
				bombNum += 1

		# Counts the amount of bombs adjacent to each button
		# For every row in the grid
		for row in range(rows):
			# For every col in the grid
			for col in range(cols):
				# If there's not a bomb in that spot
				if self.grid[row][col] != 'X':
					if col == 0:
						if row == 0: # First column, first row
							# If it's adjacent spots have a bomb
							if self.grid[row][col+1] == 'X':
								# Increment the adjacent bomb counter
								adj+=1
							if self.grid[row+1][col+1] == 'X':
								adj+=1
							if self.grid[row+1][col] == 'X':
								adj+=1
						elif row == rows-1: # First column, last row
							if self.grid[row-1][col] == 'X':
								adj+=1
							if self.grid[row-1][col+1] == 'X':
								adj+=1
							if self.grid[row][col+1] == 'X':
								adj+=1
						else: # First column, rows between 0 and 9
							if self.grid[row-1][col] == 'X':
								adj+=1
							if self.grid[row-1][col+1] == 'X':
								adj+=1
							if self.grid[row][col+1] == 'X':
								adj+=1
							if self.grid[row+1][col+1] == 'X':
								adj+=1
							if self.grid[row+1][col] == 'X':
								adj+=1
					elif col == rows-1:
						if row == 0: # Last column, first row
							if self.grid[row+1][col] == 'X':
								adj+=1
							if self.grid[row+1][col-1] == 'X':
								adj+=1
							if self.grid[row][col-1] == 'X':
								adj+=1
						elif row == rows-1: # Last column, last row
							if self.grid[row-1][col-1] == 'X':
								adj+=1
							if self.grid[row-1][col] == 'X':
								adj+=1
							if self.grid[row][col-1] == 'X':
								adj+=1
						else: # Last column, rows between 0 and 9
							if self.grid[row-1][col-1] == 'X':
								adj+=1
							if self.grid[row-1][col] == 'X':
								adj+=1
							if self.grid[row+1][col] == 'X':
								adj+=1
							if self.grid[row+1][col-1] == 'X':
								adj+=1
							if self.grid[row][col-1] == 'X':
								adj+=1
					else:
						if row == 0: # Columns between 0 and 9 and first row
							if self.grid[row][col+1] == 'X':
								adj+=1
							if self.grid[row+1][col+1] == 'X':
								adj+=1
							if self.grid[row+1][col] == 'X':
								adj+=1
							if self.grid[row+1][col-1] == 'X':
								adj+=1
							if self.grid[row][col-1] == 'X':
								adj+=1
						elif row == rows-1: # Columns between 0 and 9 and last row
							if self.grid[row-1][col-1] == 'X':
								adj+=1
							if self.grid[row-1][col] == 'X':
								adj+=1
							if self.grid[row-1][col+1] == 'X':
								adj+=1
							if self.grid[row][col+1] == 'X':
								adj+=1
							if self.grid[row][col-1] == 'X':
								adj+=1
						else: # Columns between 0 and 9 and rows between 0 and 9
							if self.grid[row-1][col-1] == 'X':
								adj+=1
							if self.grid[row-1][col] == 'X':
								adj+=1
							if self.grid[row-1][col+1] == 'X':
								adj+=1
							if self.grid[row][col+1] == 'X':
								adj+=1
							if self.grid[row+1][col+1] == 'X':
								adj+=1
							if self.grid[row+1][col] == 'X':
								adj+=1
							if self.grid[row+1][col-1] == 'X':
								adj+=1
							if self.grid[row][col-1] == 'X':
								adj+=1

					# Add adjacent bomb count to the contents of that spot
					self.grid[row][col] += adj
				# Start over the counter
				adj = 0


	# Returns what's in the button clicked
	def getSquare(self, row, col):
		return self.grid[row][col]


	# Returns current state of the game
	def getGameState(self, count, row, col):
		# If a button with a bomb is clicked, return 0
		if self.grid[row][col] == 'X':
			return 0

		# If the max amount of moves made has been hit, return 1
		if count == 90:
			return 1