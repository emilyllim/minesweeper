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
		# Counts number of bombs added to the board
		bombNum = 0

		while bombNum != 10:
			# Randomly add bombs to certain buttons
			# For location for one bomb:
			i = random.randint(0, rows-1)
			j = random.randint(0, cols-1)
			if self.grid[i][j] != 'X':
				self.grid[i][j] = 'X'
				bombNum += 1
				print(f"Random row {i} and random col {j}")


		for row in range(len(self.grid)):
			for col in range(len(self.grid)):
				#print(f"Row {row} and col {col}")
				print(f"{self.grid[row][col]}")
				# if grid[row][col+1] == 'X':
				# 	grid[row][col] += 1

		# Add number of bombs around a certain button




	def reveal(self, row, col):
		# Reveal what's in the button clicked

		return self.grid[row][col]




	# def getSquare():
		# Return the current state of the button clicked


	# def getMoveCount():
		# Return the number of moves made


	# def getGameState():
		# Current state of the game

