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
		font = QFont("Arial", 30, QFont.Bold)
		self.label.setFont(font)
		layoutH.addWidget(self.label)
		# Add it to the vertical layout
		layoutV.addLayout(layoutH)
		# Set widget to the vertical layout
		widget.setLayout(layoutV)
		# Create grid
		gridLayout = QGridLayout()

		# Holds references to the buttons
		self.buttons = []
		# Holds count of number of buttons clicked
		self.clickCount = 0

		# 100 buttons are created
		for i in range(100):
			button = QPushButton()
			button.setText(" ")
			font = QFont("Arial", 30, QFont.Bold)
			button.setFont(font)
			button.setStyleSheet("background-color : light gray")
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
			gridLayout.addWidget(self.buttons[i], row, col)
		# Add grid to the vertical layout
		layoutV.addLayout(gridLayout)

		# Add a menu to allow start of a new game
		menu = self.menuBar().addMenu("Options")
		newAct = QAction("New Game", self, shortcut=QKeySequence.New, triggered=self.newGame)
		menu.addAction(newAct)
		menu.addSeparator()
		# And an option to exit the game
		quitAct = QAction("Exit", self, shortcut=QKeySequence.Quit, triggered=self.close)
		menu.addAction(quitAct)

		# Model that keeps track of the actual game
		self.model = MineModel()
		# Call the code to start a new game
		self.newGame()


	def newGame(self):
		print("New game!");
		# Set all buttons to true
		for button in self.buttons:
			button.setEnabled(True)
			button.setText(" ")
			button.setStyleSheet("background-color : light gray")
		# Model generates a new game
		self.model.newGame()


	def buttonClicked(self):
		# Gets each button was clicked
		clicked = self.sender()
		self.clickCount += 1
		# Row and col and equal to the row and col button clicked is in
		row = clicked.property("myRow")
		col = clicked.property("myCol")

		square = str(self.model.getSquare(row, col))
		if square == 'X':
			clicked.setStyleSheet("background-color : red")
		else:
			clicked.setStyleSheet("background-color : blue")

		if self.model.getGameState(self.clickCount, row, col) == 0:
			print("You lost!")

		if self.model.getGameState(self.clickCount, row, col) == 1:
			print("You won!")


		# Button clicked now shows a bomb or how many bombs are adjacent
		clicked.setText(square)

		# Button can't be clicked anymore
		clicked.setEnabled(False)

		# Tell model of which button was clicked
		# self.model.reveal(row, col)