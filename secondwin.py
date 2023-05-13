from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton
class SecondWin (QWidget):
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
        self.fio = QLabel(txt_name)
        self.let = QLabel(txt_age)
        self.instruction = QLabel()
        self.instruction1 = QLabel()
        self.instruction2 = QLabel()
        self.button1 = QPushButton()
        self.button2 = QPushButton()
        self.button3 = QPushButton()
        self.send_button = QPushButton(txt_sendresults)
        self.pole = QLineEdit()
        self.pole1 = QLineEdit()
        self.pole2 = QLineEdit()
        self.pole3 = QLineEdit()
        self.pole4 = QLineEdit()
        self.h_line = QHBoxLayout()
        self.r_line = QHBoxLayout()
        self.l_line = QHBoxLayout()
        self.l_line.addWidget(self.fio)
        self.l_line.addWidget(self.pole)
        self.l_line.addWidget(self.let)
        self.l_line.addWidget(self.pole1)
        self.l_line.addWidget(self.instructions)
        self.l_line.addWidget(self.button)
        self.r_line.addWidget(self.timer)
        self.h_line.addWidget(self.l_line)
        self.h_line.addWidget(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        self.send_button.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.fw = FinalWin()

app = QApplication([])
sw = SecondWin()
app.exec_()



