import random

class MineModel:
	def __init__(self):
		# Start a new game
		self.newGame()

	def newGame(self):
		rows = 10
		cols = 10
		# Each button is set 0, meaning they haven't been clicked yet
		self.grid = [[0]*(cols) for i in range(rows)]
		# Bombs in the board are represented as an X
		bomb = 'X'
		# Counts number of bombs added to the board
		bombNum = 0
		# Stores bombs adjacent to current button
		adj = 0

		while bombNum != 10:
			# Randomly add bombs to certain buttons
			# For location for one bomb:
			i = random.randint(0, rows-1)
			j = random.randint(0, cols-1)
			if self.grid[i][j] != bomb:
				self.grid[i][j] = bomb
				bombNum += 1
				#print(f"Random row {i} and random col {j}")


		for row in range(rows):
			for col in range(cols):
				#print(f"Row {row} and col {col}")
				if self.grid[row][col] != bomb:
					if col == 0:
						if row == 0: # First row
							if self.grid[row][col+1] == bomb:
								adj+=1
							if self.grid[row+1][col+1] == bomb:
								adj+=1
							if self.grid[row+1][col] == bomb:
								adj+=1
						elif row == rows-1: # Last row
							if self.grid[row-1][col] == bomb:
								adj+=1
							if self.grid[row-1][col+1] == bomb:
								adj+=1
							if self.grid[row][col+1] == bomb:
								adj+=1
						else: # Rows in between
							if self.grid[row-1][col] == bomb:
								adj+=1
							if self.grid[row-1][col+1] == bomb:
								adj+=1
							if self.grid[row][col+1] == bomb:
								adj+=1
							if self.grid[row+1][col+1] == bomb:
								adj+=1
							if self.grid[row+1][col] == bomb:
								adj+=1
					elif col == rows-1:
						if row == 0:
							if self.grid[row+1][col] == bomb:
								adj+=1
							if self.grid[row+1][col-1] == bomb:
								adj+=1
							if self.grid[row][col-1] == bomb:
								adj+=1
						elif row == rows-1:
							if self.grid[row-1][col-1] == bomb:
								adj+=1
							if self.grid[row-1][col] == bomb:
								adj+=1
							if self.grid[row][col-1] == bomb:
								adj+=1
						else:
							if self.grid[row-1][col-1] == bomb:
								adj+=1
							if self.grid[row-1][col] == bomb:
								adj+=1
							if self.grid[row+1][col] == bomb:
								adj+=1
							if self.grid[row+1][col-1] == bomb:
								adj+=1
							if self.grid[row][col-1] == bomb:
								adj+=1
					else:
						if row == 0:
							if self.grid[row][col+1] == bomb:
								adj+=1
							if self.grid[row+1][col+1] == bomb:
								adj+=1
							if self.grid[row+1][col] == bomb:
								adj+=1
							if self.grid[row+1][col-1] == bomb:
								adj+=1
							if self.grid[row][col-1] == bomb:
								adj+=1
						elif row == rows-1:
							if self.grid[row-1][row-1] == bomb:
								adj+=1
							if self.grid[row-1][col] == bomb:
								adj+=1
							if self.grid[row-1][col+1] == bomb:
								adj+=1
							if self.grid[row][col+1] == bomb:
								adj+=1
							if self.grid[row][col-1] == bomb:
								adj+=1
						else:
							if self.grid[row-1][col-1] == bomb:
								adj+=1
							if self.grid[row-1][col] == bomb:
								adj+=1
							if self.grid[row-1][col+1] == bomb:
								adj+=1
							if self.grid[row][col+1] == bomb:
								adj+=1
							if self.grid[row+1][col+1] == bomb:
								adj+=1
							if self.grid[row+1][col] == bomb:
								adj+=1
							if self.grid[row+1][col-1] == bomb:
								adj+=1
							if self.grid[row][col-1] == bomb:
								adj+=1


					self.grid[row][col] += adj
					adj = 0



	# Returns what's in the button clicked
	def reveal(self, row, col):
		return self.grid[row][col]


	# def getSquare():
		# Return the current state of the button clicked


	# def getMoveCount():
		# Return the number of moves made


	# def getGameState():
		# Current state of the game

