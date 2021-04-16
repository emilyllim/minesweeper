from PyQt5.QtWidgets import QApplication
from MineWindow import *

app = QApplication([])
window = MineWindow()
window.show()
app.exec_()