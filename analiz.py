from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QLabel, QPushButton, \
    QComboBox, QWidget

from widget_analiz.push_button import ButtonBack


class WindowAnaliz(QWidget):
    def __init__(self, parent):
        super(WindowAnaliz, self).__init__(parent)
        self.setGeometry(0, 0, 1920, 1080)
        self.move(0, 0)
        # инициализация кнопки назад в меню
        self.button_back = ButtonBack(self, parent)
