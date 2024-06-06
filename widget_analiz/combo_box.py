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

        self.activated[str].connect(lambda: self.update_tabs(parent))

    def update_tabs(self, parent):
        if self.currentIndex() == 0:
            self.show_cell(True, parent)
            self.show_circle(False, parent)
            self.show_triangle(False, parent)
            self.show_hexagon(False, parent)
        elif self.currentIndex() == 1:
            self.show_hexagon(True, parent)
            self.show_cell(False, parent)
            self.show_circle(False, parent)
            self.show_triangle(False, parent)
        elif self.currentIndex() == 2:
            self.show_triangle(True, parent)
            self.show_cell(False, parent)
            self.show_circle(False, parent)
            self.show_hexagon(False, parent)
        elif self.currentIndex() == 3:
            self.show_circle(True, parent)
            self.show_cell(False, parent)
            self.show_triangle(False, parent)
            self.show_hexagon(False, parent)

    def show_cell(self, flag, parent):
        parent.tabs_cell.setVisible(flag)

    def show_circle(self, flag, parent):
        parent.tabs_circle.setVisible(flag)

    def show_triangle(self, flag, parent):
        parent.tabs_triangle.setVisible(flag)

    def show_hexagon(self, flag, parent):
        parent.tabs_hexagon.setVisible(flag)
