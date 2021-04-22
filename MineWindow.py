from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from MineModel import *

# Interface
class MineWindow(QMainWindow):
	def __init__(self):
		super(MineWindow, self).__init__()

		# Central widget created
		widget = QWidget()
		self.setCentralWidget(widget)

		# QVBoxLayout created
		layoutV = QVBoxLayout()
		# Add a QHBoxLayout
		layoutH = QHBoxLayout()

		# Label showing the number of bombs in grid
		self.label = QLabel("Bombs: 10")
		# Set font of the label
		font = QFont("Arial", 30, QFont.Bold)
		self.label.setFont(font)
		# Label added to the horizontal layout
		layoutH.addWidget(self.label)

		# Holds count of number of buttons clicked
		self.moveCount = 0
		# Label showing number of moves made
		self.moveLabel = QLabel("Moves Made: " + str(self.moveCount))
		self.moveLabel.setFont(font)
		layoutH.addWidget(self.moveLabel)

		# Button to press if player wants to flag buttons
		self.flagButton = QPushButton()
		self.flagButton.setText("Flag")
		font = QFont("Arial", 20, QFont.Bold)
		self.flagButton.setFont(font)
		# Button is gray when flagging mode is off
		self.flagButton.setStyleSheet("background-color : light gray")
		# Property that tells if flagging mode is on or off
		self.flagButton.setProperty("on", False)
		# Set a fixed size for the button
		self.flagButton.setFixedSize(QSize(100, 50))
		# Flag clicked function activated when button is clicked
		self.flagButton.clicked.connect(self.flagClicked)
		layoutH.addWidget(self.flagButton)

		# Add horizontal layout to the vertical layout
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
			# Buttons originally have no text and are gray
			button.setText(" ")
			font = QFont("Arial", 35, QFont.Bold)
			button.setFont(font)
			button.setStyleSheet("background-color : light gray")
			# Button sizes fixed to be square
			button.setFixedSize(QSize(100, 100))
			# Tells which button was clicked
			button.clicked.connect(self.buttonClicked)
			# These buttons are added to the buttons list
			self.buttons.append(button)
			# 10 by 10 grid
			row = i // 10
			col = i % 10
			# Properties that contain what row and col the button is in
			button.setProperty("myRow", row)
			button.setProperty("myCol", col)
			# Property for what color the button currently is
			button.setProperty("color", "light gray")
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

		# Model that keeps track of the contents of the grid
		self.model = MineModel()
		# Start a new game
		self.newGame()


	# Starts a new game
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
		self.moveCount = 0
		# Set bomb label to 10
		self.label.setText("Bombs: 10")
		# Reset moves label
		self.moveLabel.setText("Moves Made: " + str(self.moveCount))
		# Model generates a new game
		self.model.newGame()

	# Runs each time a button in the grid is clicked
	def buttonClicked(self):
		# Gets the button that was clicked
		clicked = self.sender()
		# Row and col and equal to the row and col that button is in
		row = clicked.property("myRow")
		col = clicked.property("myCol")

		# If flag mode is not on
		if self.flagButton.property("on") == False:
			# Get the contents of the square
			square = str(self.model.getSquare(row, col))
			# If there's a bomb in the square
			if square == 'X':
				# Color of button is set to red
				clicked.setStyleSheet("background-color : red")
			else:
				# Color of button is set to blue
				clicked.setStyleSheet("background-color : blue")
			# Button clicked now shows a bomb or how many bombs are adjacent
			clicked.setText(square)

			# If a button with a bomb was clicked, game is over
			if self.model.getGameState(self.moveCount, row, col) == 0:
				self.label.setText("Game Over!")
				# Deactivate all the buttons
				for button in self.buttons:
					button.setEnabled(False)
				self.flagButton.setEnabled(False)
				self.flagButton.setStyleSheet("background-color : light gray")
			else:
				# Increment move counter
				self.moveCount += 1
				self.moveLabel.setText("Moves Made: " + str(self.moveCount))

			# If all buttons that aren't bombs have been clicked, game is won
			if self.model.getGameState(self.moveCount, row, col) == 1:
				self.label.setText("You Won!")
				# Deactivate all the buttons
				for button in self.buttons:
					button.setEnabled(False)
				self.flagButton.setEnabled(False)
				self.flagButton.setStyleSheet("background-color : light gray")

			# Button can't be clicked anymore
			clicked.setEnabled(False)
		# If flag mode is on
		else:
			# Change button in grid to green to flag it
			if clicked.property("color") == "light gray":
				clicked.setStyleSheet("background-color : green")
				clicked.setProperty("color", "green")
			else:
				# Change button back to gray if it was green to unflag it
				if clicked.property("color") == "green":
					clicked.setStyleSheet("background-color : light gray")
					clicked.setProperty("color", "light gray")


	# Runs each time flag button is clicked
	def flagClicked(self):
		clicked = self.sender()

		# If flag mode was off, it is now on
		if clicked.property("on") == False:
			# Set button green and set on property to be true
			self.flagButton.setStyleSheet("background-color : green")
			self.flagButton.setProperty("on", True)
			# When flag mode is on, enable all buttons that are flagged
			for button in self.buttons:
				if button.property("color") == "green":
					button.setEnabled(True)
		# Else, flag mode is now off
		else:
			# Set button gray and set on property to be false
			self.flagButton.setStyleSheet("background-color : light gray")
			self.flagButton.setProperty("on", False)
			# When flag mode is off, disable all buttons that are flagged
			for button in self.buttons:
				if button.property("color") == "green":
					button.setEnabled(False)