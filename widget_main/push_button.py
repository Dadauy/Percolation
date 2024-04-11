from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton


class ButtonViewModel(QPushButton):
    def __init__(self, parent=None):
        super(ButtonViewModel, self).__init__(parent)
        self.setGeometry(0, 0, 300, 100)
        self.move(800, 200)
        font = QFont()
        font.setPointSize(16)
        self.setFont(font)
        self.setText("Моделирование")

    def view_model(self, parent):
        parent.WindowModeling.setVisible(True)
        parent.WindowAnaliz.setVisible(False)
        parent.ButtonModel.setVisible(False)
        parent.ButtonAnaliz.setVisible(False)


class ButtonViewAnaliz(QPushButton):
    def __init__(self, parent=None):
        super(ButtonViewAnaliz, self).__init__(parent)
        self.setGeometry(0, 0, 300, 100)
        self.move(800, 350)
        font = QFont()
        font.setPointSize(16)
        self.setFont(font)
        self.setText("Анализ")

    def view_analiz(self, parent):
        parent.WindowModeling.setVisible(False)
        parent.WindowAnaliz.setVisible(True)
        parent.ButtonModel.setVisible(False)
        parent.ButtonAnaliz.setVisible(False)
