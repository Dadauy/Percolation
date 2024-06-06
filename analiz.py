from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QLabel, QPushButton, \
    QComboBox, QWidget

from widget_analiz.push_button import ButtonBack
from widget_analiz.label import LabelCell
from widget_analiz.combo_box import ComboBoxCell
from tabs.tab_cell import TabsWidgetCell
from tabs.tab_circle import TabsWidgetCircle
from tabs.tab_hexagon import TabsWidgetHexagon
from tabs.tab_triangle import TabsWidgetTriangle


class WindowAnaliz(QWidget):
    def __init__(self, parent):
        super(WindowAnaliz, self).__init__(parent)
        self.setGeometry(0, 0, 1920, 1080)
        self.move(0, 0)
        # инициализация кнопки назад в меню
        self.button_back = ButtonBack(self, parent)
        # инициализация бокса с сетками
        self.combo_box_cell = ComboBoxCell(self)
        # инициализация лейбла сетки
        self.label_cell = LabelCell(self)
        # инициализация табов
        self.tabs_cell = TabsWidgetCell(self)
        self.tabs_hexagon = TabsWidgetHexagon(self)
        self.tabs_triangle = TabsWidgetTriangle(self)
        self.tabs_circle = TabsWidgetCircle(self)
        self.tabs_hexagon.setVisible(False)
        self.tabs_triangle.setVisible(False)
        self.tabs_circle.setVisible(False)
