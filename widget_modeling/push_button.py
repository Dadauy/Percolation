import numpy
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton
from percolations_algorithms.circle import CirclePercolation
from percolations_algorithms.triangle import TrianglePercolation
from percolations_algorithms.point import RandomPointPercolation
from percolations_algorithms.hexagon import HexagonsPercolation
from percolations_algorithms.cell import SquarePercolation


class ButtonModeling(QPushButton):
    def __init__(self, parent=None):
        super(ButtonModeling, self).__init__(parent)
        self.setGeometry(0, 0, 300, 50)
        self.move(1550, 400)
        font = QFont()
        font.setPointSize(16)
        self.setFont(font)
        self.setText("Смоделировать")

        # TODO: настроить цвет кнопки смоделировать
        # self.setStyleSheet('background-color: red;')
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
        elif parent.combo_box_cell.currentIndex() == 3:
            parent.percolation = CirclePercolation(int(parent.horizontal_slider_size_circle.value()))
        elif parent.combo_box_cell.currentIndex() == 4:
            parent.percolation = RandomPointPercolation(float(parent.horizontal_slider_probability.value() / 1000))
        parent.color_lst = numpy.array([numpy.random.randint(0, 255, 3) for i in
                                        range(len(parent.percolation.cell))])

        parent.idx_cell = parent.combo_box_cell.currentIndex()

        parent.repaint()


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

    def move_back(self, parent2):
        parent2.WindowModeling.setVisible(False)
        parent2.ButtonModel.setVisible(True)
        parent2.ButtonAnaliz.setVisible(True)
