import numpy
import sys
import traceback

from percolation_algorithms import SquarePercolation, HexagonsPercolation, TrianglePercolation, CirclePercolation
import random

from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QLabel, QGraphicsView, QPushButton, \
    QGraphicsEllipseItem, QGraphicsScene, QWidget, QOpenGLWidget, QComboBox
from PyQt5.QtGui import QBrush, QPen, QPainter, QColor, QFont
from PyQt5.QtCore import Qt
from paint_percolation import paint_percolation_cell, paint_percolation_hexagon, paint_percolation_triangle, \
    paint_percolation_circle


class PainterPercolation(QPainter):
    def __init__(self, parent=None):
        super(PainterPercolation, self).__init__(parent)

    def paint_board(self):
        self.setBrush(QColor(255, 255, 255))
        self.drawRect(50, 50, 1450, 850)

    def paint_percolation(self, percolation, color_lst, idx_cell):
        if idx_cell == 0:
            paint_percolation_cell(self, percolation, color_lst)
        elif idx_cell == 1:
            paint_percolation_hexagon(self, percolation, color_lst)
        elif idx_cell == 2:
            paint_percolation_triangle(self, percolation, color_lst)
        elif idx_cell == 3:
            paint_percolation_circle(self, percolation, color_lst)


class SliderSize(QSlider):
    def __init__(self, parent=None):
        super(SliderSize, self).__init__(parent)
        self.setGeometry(0, 0, 300, 50)
        self.move(1550, 200)
        self.setOrientation(Qt.Horizontal)
        self.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.setRange(0, 50)
        self.setSingleStep(5)

        self.valueChanged.connect(lambda: self.update_value_size(parent))

    def update_value_size(self, parent):
        parent.label_size.setText(f"N: {self.value()}")


class SliderProbability(QSlider):
    def __init__(self, parent=None):
        super(SliderProbability, self).__init__(parent)
        self.setGeometry(0, 0, 300, 50)
        self.move(1550, 300)
        self.setOrientation(Qt.Horizontal)
        self.setRange(0, 1000)
        self.setSingleStep(50)
        self.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.valueChanged.connect(lambda: self.update_value_probability(parent))

    def update_value_probability(self, parent):
        parent.label_probability.setText(f"P: {self.value() / 1000:.3f}")


class LabelSize(QLabel):
    def __init__(self, parent=None):
        super(LabelSize, self).__init__(parent)
        self.setGeometry(0, 0, 300, 50)
        self.move(1550, 250)
        font = QFont()
        font.setPointSize(16)
        self.setFont(font)
        self.setText("N: 0")


class LabelSizeCircle(QLabel):
    def __init__(self, parent=None):
        super(LabelSizeCircle, self).__init__(parent)
        self.setGeometry(0, 0, 300, 50)
        self.move(1550, 250)
        font = QFont()
        font.setPointSize(16)
        self.setFont(font)
        self.setText("R: 0")


class SliderSizeCircle(QSlider):
    def __init__(self, parent=None):
        super(SliderSizeCircle, self).__init__(parent)
        self.setGeometry(0, 0, 300, 50)
        self.move(1550, 200)
        self.setOrientation(Qt.Horizontal)
        self.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.setRange(0, 100)
        self.setSingleStep(5)

        self.valueChanged.connect(lambda: self.update_value_size(parent))

    def update_value_size(self, parent):
        parent.label_size_circle.setText(f"R: {self.value()}")


class LabelCell(QLabel):
    def __init__(self, parent=None):
        super(LabelCell, self).__init__(parent)
        self.setGeometry(0, 0, 300, 50)
        self.move(1550, 100)
        font = QFont()
        font.setPointSize(16)
        self.setFont(font)
        self.setText("Сетка: ")


class LabelProbability(QLabel):
    def __init__(self, parent=None):
        super(LabelProbability, self).__init__(parent)
        self.setGeometry(0, 0, 300, 50)
        self.move(1550, 350)
        font = QFont()
        font.setPointSize(16)
        self.setFont(font)
        self.setText("P: 0.000")


class ButtonModeling(QPushButton):
    def __init__(self, parent=None):
        super(ButtonModeling, self).__init__(parent)
        self.setGeometry(0, 0, 300, 50)
        self.move(1550, 400)
        font = QFont()
        font.setPointSize(16)
        self.setFont(font)
        self.setText("Смоделировать")
        self.clicked.connect(lambda: self.modeling_percolation(parent))

    def modeling_percolation(self, parent):
        if parent.combo_box_cell.currentIndex() == 0:
            parent.percolation = SquarePercolation(int(parent.horizontal_slider_size.value()),
                                                   float(parent.horizontal_slider_probability.value() / 1000))
        elif parent.combo_box_cell.currentIndex() == 1:
            parent.percolation = HexagonsPercolation(int(parent.horizontal_slider_size.value()),
                                                     float(parent.horizontal_slider_probability.value() / 1000))
        elif parent.combo_box_cell.currentIndex() == 2:
            parent.percolation = TrianglePercolation(int(parent.horizontal_slider_size.value()),
                                                     float(parent.horizontal_slider_probability.value() / 1000))
        elif parent.combo_box_cell.currentIndex() == 2:
            parent.percolation = CirclePercolation(int(parent.horizontal_slider_size_circle.value()))
        parent.color_lst = numpy.array([numpy.random.randint(0, 255, 3) for i in
                                        range(len(parent.percolation.cell))])

        parent.idx_cell = parent.combo_box_cell.currentIndex()

        parent.repaint()


class ComboBoxCell(QComboBox):
    def __init__(self, parent=None):
        super(ComboBoxCell, self).__init__(parent)
        self.setGeometry(0, 0, 300, 50)
        self.move(1550, 150)
        font = QFont()
        font.setPointSize(16)
        self.setFont(font)
        self.addItem("Квадратная")
        self.addItem("Гексагональная")
        self.addItem("Треугольная")
        self.addItem("Случайная(с кругами)")
        self.flag_update_label_and_slider = False

        self.activated[str].connect(lambda: self.update_range_size(parent))

    def update_range_size(self, parent):
        if self.currentIndex() == 3:
            self.flag_update_label_and_slider = True
            self.show_widget_N_P(False, parent)
            self.show_widget_R(True, parent)
        else:
            if self.flag_update_label_and_slider:
                self.show_widget_R(False, parent)
                self.show_widget_N_P(True, parent)
            if self.currentIndex() == 0:
                parent.horizontal_slider_size.setRange(0, 50)
            elif self.currentIndex() == 1:
                parent.horizontal_slider_size.setRange(0, 10)
            elif self.currentIndex() == 2:
                parent.horizontal_slider_size.setRange(0, 50)

    def show_widget_N_P(self, flag, parent):
        parent.horizontal_slider_size.setVisible(flag)
        parent.horizontal_slider_probability.setVisible(flag)
        parent.label_probability.setVisible(flag)
        parent.label_size.setVisible(flag)

    def show_widget_R(self, flag, parent):
        parent.label_size_circle.setVisible(flag)
        parent.horizontal_slider_size_circle.setVisible(flag)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # настйроки главного экрана
        self.setGeometry(0, 0, 1920, 1080)
        self.move(0, 0)
        self.setWindowTitle("Моделятор перколяций")
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

    def paintEvent(self, event):
        painter = PainterPercolation(self)
        painter.paint_board()
        painter.paint_percolation(self.percolation, self.color_lst, self.idx_cell)


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("Oбнаружена ошибка !:", tb)


#    QtWidgets.QApplication.quit()             # !!! если вы хотите, чтобы событие завершилось


sys.excepthook = excepthook

if __name__ == "__main__":
    app = QApplication([])
    my_window = MyWindow()
    my_window.show()
    app.exec()
