import numpy
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QComboBox


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
        # self.addItem("Случайная(с точками)")

        self.activated[str].connect(lambda: self.update_range_size(parent))

    def update_range_size(self, parent):
        parent.percolation = None
        parent.color_lst = None
        parent.idx_cell = -1
        parent.flag_info = False
        parent.answer_circle = None
        if self.currentIndex() == 3:
            self.show_widget_N(False, parent)
            self.show_widget_P(False, parent)
            self.show_widget_R(True, parent)
            parent.repaint()
        elif self.currentIndex() == 4:
            self.show_widget_N(False, parent)
            self.show_widget_P(True, parent)
            self.show_widget_R(False, parent)
            parent.repaint()
        else:
            self.show_widget_R(False, parent)
            self.show_widget_P(True, parent)
            self.show_widget_N(True, parent)
            if self.currentIndex() == 0:
                parent.horizontal_slider_size.setRange(0, 50)
            elif self.currentIndex() == 1:
                parent.horizontal_slider_size.setRange(0, 10)
            elif self.currentIndex() == 2:
                parent.horizontal_slider_size.setRange(0, 50)
            parent.repaint()

    def show_widget_N(self, flag, parent):
        parent.horizontal_slider_size.setVisible(flag)
        parent.label_size.setVisible(flag)

    def show_widget_P(self, flag, parent):
        parent.horizontal_slider_probability.setVisible(flag)
        parent.label_probability.setVisible(flag)

    def show_widget_R(self, flag, parent):
        parent.label_size_circle.setVisible(flag)
        parent.horizontal_slider_size_circle.setVisible(flag)
