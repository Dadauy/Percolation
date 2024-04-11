import numpy
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSlider, QLabel, QPushButton, QWidget, QComboBox

from widget_modeling.painter import PainterPercolation
from widget_modeling.push_button import ButtonModeling, ButtonBack
from widget_modeling.slider import SliderSize, SliderProbability, SliderSizeCircle
from widget_modeling.label import LabelProbability, LabelSize, LabelCell, LabelSizeCircle
from widget_modeling.combo_box import ComboBoxCell


class WindowModeling(QWidget):
    def __init__(self, parent=None):
        super(WindowModeling, self).__init__(parent)
        # настйроки главного экрана
        self.setGeometry(0, 0, 1920, 1080)
        self.move(0, 0)
        # инициализация лабла с сеткой
        self.label_cell: QLabel = LabelCell(self)
        # инициализация лейбла с размером сетки
        self.label_size: QLabel = LabelSize(self)
        # инициализация слайдера с размером сетки
        self.horizontal_slider_size: QSlider = SliderSize(self)
        # инициализация лейбла с размером сетки
        self.label_probability: QLabel = LabelProbability(self)
        # инициализация слайдера с вероятность
        self.horizontal_slider_probability: QSlider = SliderProbability(self)
        # инициализация кнопки моделирования перколяций
        self.button_modeling: QPushButton = ButtonModeling(self)
        # инициализация комбо-бокса
        self.combo_box_cell = ComboBoxCell(self)
        # инициализация лебла с размером кругов
        self.label_size_circle: QLabel = LabelSizeCircle(self)
        self.label_size_circle.setVisible(False)
        # инициализация слайдера с размеров кругов
        self.horizontal_slider_size_circle: QSlider = SliderSizeCircle(self)
        self.horizontal_slider_size_circle.setVisible(False)
        # инициализация перколяций
        self.percolation = numpy.array([])
        self.color_lst = numpy.array([])
        self.idx_cell = -1
        # TODO: настроить цвет всего окна
        # self.setStyleSheet('background-color: rgb(100, 133, 202);')
        # инициализация кнопки назад
        self.button_back = ButtonBack(self, parent)

    def paintEvent(self, event):
        painter = PainterPercolation(self)
        if 0 <= self.combo_box_cell.currentIndex() <= 2:
            painter.paint_board()
        else:
            painter.paint_second_board()
        painter.paint_percolation(self.percolation, self.color_lst, self.idx_cell)
