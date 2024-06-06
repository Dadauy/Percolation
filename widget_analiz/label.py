from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel


class LabelCell(QLabel):
    def __init__(self, parent=None):
        super(LabelCell, self).__init__(parent)
        self.setGeometry(0, 0, 300, 50)
        self.move(1550, 100)
        font = QFont()
        font.setPointSize(16)
        self.setFont(font)
        self.setText("Сетка: ")
