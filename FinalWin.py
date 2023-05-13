from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton
class FinalWin (QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUI(self):
        self.text_one = QLabel()
        self.text_two = QLabel()
        self.line_v = QVBoxLayout()
        self.line_v.addWidget(self.text_one)
        self.line_v.addWidget(self.text_two)
        self.setLayout(self.line_v)
app = QApplication([])
fw = FinalWin()
app.exec_()


