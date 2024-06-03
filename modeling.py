import numpy
from PyQt5.QtWidgets import QSlider, QLabel, QPushButton, QWidget

from info_of_claster.cell_info import info_cell
from info_of_claster.hexagon_info import info_hexagon
from info_of_claster.triangle_info import info_triangle
from widget_modeling.combo_box import ComboBoxCell
from widget_modeling.label import LabelProbability, LabelSize, LabelCell, LabelSizeCircle
from widget_modeling.painter import PainterPercolation
from widget_modeling.push_button import ButtonModeling, ButtonBack
from widget_modeling.slider import SliderSize, SliderProbability, SliderSizeCircle


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
        """
        ТУТ ДАННЫЕ
        """
        self.percolation = None
        self.color_lst = None
        self.idx_cell = -1
        # инициализация кнопки назад
        self.button_back = ButtonBack(self, parent)
        # отрисовка инфы о кластере
        """
        ТУТ ДАННЫЕ
        """
        self.flag_info = False  # если надо вывести инфу по кластеру
        self.color_claster = ()  # список цветов
        self.cnt_v = 0  # количество вершин
        self.center_mass = (0, 0)  # центр масс
        self.radius_claster = 0  # радиус кластера

    def paintEvent(self, event):
        painter = PainterPercolation(self)
        if 0 <= self.combo_box_cell.currentIndex() <= 2:  # для сеток
            painter.paint_first_board()
        else:  # для рандома
            painter.paint_second_board()
        painter.paint_percolation(self.percolation, self.color_lst, self.idx_cell)  # отрисовка узлов и связей
        if self.flag_info:
            if 0 <= self.combo_box_cell.currentIndex() <= 2:  # для сеток
                painter.paint_info_claster(self.color_claster, self.cnt_v, self.center_mass, self.radius_claster)
                painter.paint_radius_claster(self.percolation, self.center_mass, self.radius_claster, self.idx_cell)
            else:  # для рандома
                painter.paint_answer_circle(self.percolation)

    def mousePressEvent(self, a0):
        if self.percolation is None:
            return
        x, y = a0.pos().x(), a0.pos().y()  # корды мыши
        if self.combo_box_cell.currentIndex() == 0:
            info_cell(self, self.percolation, self.color_lst, x, y)
        elif self.combo_box_cell.currentIndex() == 1:
            info_hexagon(self, self.percolation, self.color_lst, x, y)
        elif self.combo_box_cell.currentIndex() == 2:
            info_triangle(self, self.percolation, self.color_lst, x, y)
