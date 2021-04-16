from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from MineModel import *

# Interface

class MineWindow(QMainWindow):
	def __init__(self):
		super(MineWindow, self).__init__()

		widget = QWidget()
		self.setCentralWidget(widget)

		# QVBoxLayout created
		layoutV = QVBoxLayout()
		# Add a QHBoxLayout with a QLabel
		layoutH = QHBoxLayout()
		self.label = QLabel("Score")
		layoutH.addWidget(self.label)
		# Add it to the vertical layout
		layoutV.addLayout(layoutH)
		# Set widget to the vertical layout
		widget.setLayout(layoutV)
		# Create grid
		grid = QGridLayout()

		# Holds references to the buttons
		self.buttons = []

		# 100 buttons are created
		for i in range(100):
			button = QPushButton()
			# Tells which button was clicked
			button.clicked.connect(self.buttonClicked)
			# These buttons are added to the buttons list
			self.buttons.append(button)
			# `10 by 10 grid
			row = i // 10
			col = i % 10
			# Properties that contain what row and col the button is in
			button.setProperty("myRow", row)
			button.setProperty("myCol", col)
			# Each button is added to the grid
			grid.addWidget(self.buttons[i], row, col)
		# Add grid to the vertical layout
		layoutV.addLayout(grid)

		# Model that keeps track of the actual game
		#self.model = MineModel()
		# Call the code to start a new game
		#self.newGame()


	# def newGame(self):
	# 	print("New game!");
	# 	for button in self.buttons:
	# 		button.setEnabled(true)

	# 	self.model.newGame()


	def buttonClicked(self):
		# Gets each button was clicked
		clicked = self.sender()
		# Row and col and equal to the row and col button clicked is in
		row = clicked.property("myRow")
		col = clicked.property("myCol")
		# Print the result
		print(f"Row {row} and column {col} was clicked!")


# rows =
# cols =
# grid = [[0]*(cols) for i in range(rows)]