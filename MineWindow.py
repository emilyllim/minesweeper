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
		self.label = QLabel("Bombs: 10")
		font = QFont("Arial", 30, QFont.Bold)
		self.label.setFont(font)
		layoutH.addWidget(self.label)

		# Holds count of number of buttons clicked
		self.clickCount = 0
		# Label showing number of moves made
		self.moveLabel = QLabel("Moves made: " + str(self.clickCount))
		self.moveLabel.setFont(font)
		layoutH.addWidget(self.moveLabel)

		# Button to press if player wants to flag buttons
		self.flagButton = QPushButton()
		self.flagButton.setText("Flag")
		font = QFont("Arial", 20, QFont.Bold)
		self.flagButton.setFont(font)
		self.flagButton.setStyleSheet("background-color : light gray")
		self.flagButton.setProperty("on", False)
		self.flagButton.setFixedSize(QSize(100, 50))
		self.flagButton.clicked.connect(self.flagClicked)
		layoutH.addWidget(self.flagButton)

		# Add it to the vertical layout
		layoutV.addLayout(layoutH)
		# Set widget to the vertical layout
		widget.setLayout(layoutV)
		# Create grid
		gridLayout = QGridLayout()

		# Holds references to the buttons
		self.buttons = []

		# 100 buttons are created
		for i in range(100):
			button = QPushButton()
			button.setText(" ")
			font = QFont("Arial", 35, QFont.Bold)
			button.setFont(font)
			button.setStyleSheet("background-color : light gray")
			button.setFixedSize(QSize(100, 100))
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
		# Reset all buttons
		for button in self.buttons:
			button.setEnabled(True)
			button.setText(" ")
			button.setStyleSheet("background-color : light gray")
		# Reset flag button
		self.flagButton.setEnabled(True)
		self.flagButton.setStyleSheet("background-color : light gray")
		self.flagButton.setProperty("on", False)
		# Reset buttons clicked to 0
		self.clickCount = 0
		# Set bomb label to 10
		self.label.setText("Bombs: 10")
		# Reset moves label
		self.moveLabel.setText("Moves made: " + str(self.clickCount))
		# Model generates a new game
		self.model.newGame()


	def buttonClicked(self):
		# Gets each button was clicked
		clicked = self.sender()
		self.clickCount += 1
		self.moveLabel.setText("Moves made: " + str(self.clickCount))
		# Row and col and equal to the row and col button clicked is in
		row = clicked.property("myRow")
		col = clicked.property("myCol")

		if self.flagButton.property("on") == False:
			square = str(self.model.getSquare(row, col))
			if square == 'X':
				clicked.setStyleSheet("background-color : red")
			else:
				clicked.setStyleSheet("background-color : blue")
			# Button clicked now shows a bomb or how many bombs are adjacent
			clicked.setText(square)

			# If a button with a bomb is clicked, game is over
			if self.model.getGameState(self.clickCount, row, col) == 0:
				self.label.setText("Game Over!")
				for button in self.buttons:
					button.setEnabled(False)

			# If all buttons have been clicked, game is won
			if self.model.getGameState(self.clickCount, row, col) == 1:
				self.label.setText("You Won!")

		else:
			clicked.setStyleSheet("background-color : green")

		# Button can't be clicked anymore
		clicked.setEnabled(False)

	def flagClicked(self):
		clicked = self.sender()

		if clicked.property("on") == False:
			self.flagButton.setStyleSheet("background-color : green")
			self.flagButton.setProperty("on", True)
		else:
			self.flagButton.setStyleSheet("background-color : light gray")
			self.flagButton.setProperty("on", False)
