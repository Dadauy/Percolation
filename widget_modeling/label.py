from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel


class LabelSize(QLabel):
    def __init__(self, parent=None):
        super(LabelSize, self).__init__(parent)
        self.setGeometry(0, 0, 300, 50)
        self.move(1550, 250)
        font = QFont()
        font.setPointSize(16)
        self.setFont(font)
        # TODO: настроить цвет
        # self.setStyleSheet('background-color: green;')
        self.setText("N: 0")


class LabelSizeCircle(QLabel):
    def __init__(self, parent=None):
        super(LabelSizeCircle, self).__init__(parent)
        self.setGeometry(0, 0, 300, 50)
        self.move(1550, 350)
        font = QFont()
        font.setPointSize(16)
        self.setFont(font)
        # TODO: настроить цвет
        # self.setStyleSheet('background-color: green;')
        self.setText("R: 30")


class LabelCell(QLabel):
    def __init__(self, parent=None):
        super(LabelCell, self).__init__(parent)
        self.setGeometry(0, 0, 300, 50)
        self.move(1550, 100)
        font = QFont()
        font.setPointSize(16)
        self.setFont(font)
        # TODO: настроить цвет
        # self.setStyleSheet('background-color: green;')
        self.setText("Сетка: ")


class LabelProbability(QLabel):
    def __init__(self, parent=None):
        super(LabelProbability, self).__init__(parent)
        self.setGeometry(0, 0, 300, 50)
        self.move(1550, 350)
        font = QFont()
        font.setPointSize(16)
        self.setFont(font)
        # TODO: настроить цвет
        # self.setStyleSheet('background-color: green;')
        self.setText("P: 0.000")
