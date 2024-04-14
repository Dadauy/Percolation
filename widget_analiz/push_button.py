from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton


class ButtonBack(QPushButton):
    def __init__(self, parent=None, parent2=None):
        super(ButtonBack, self).__init__(parent)
        self.setGeometry(0, 0, 100, 50)
        self.move(1800, 20)
        font = QFont()
        font.setPointSize(16)
        self.setFont(font)
        self.setText("Меню")

        # TODO: настроить цвет кнопки смоделировать
        # self.setStyleSheet('background-color: red;')
        self.clicked.connect(lambda: self.move_back(parent2))

    @staticmethod
    def move_back(parent2):
        parent2.WindowAnaliz.setVisible(False)
        parent2.ButtonModel.setVisible(True)
        parent2.ButtonAnaliz.setVisible(True)
