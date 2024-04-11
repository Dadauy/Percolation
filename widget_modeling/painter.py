from PyQt5.QtGui import QPainter, QColor

from paint_percolations.point import paint_percolation_random_point
from paint_percolations.cell import paint_percolation_cell
from paint_percolations.circle import paint_percolation_circle
from paint_percolations.triangle import paint_percolation_triangle
from paint_percolations.hexagon import paint_percolation_hexagon


class PainterPercolation(QPainter):
    def __init__(self, parent=None):
        super(PainterPercolation, self).__init__(parent)

    def paint_board(self):
        self.setBrush(QColor(255, 255, 255))
        self.drawRect(400, 50, 850, 850)

    def paint_percolation(self, percolation, color_lst, idx_cell):
        if idx_cell == 0:
            paint_percolation_cell(self, percolation, color_lst)
        elif idx_cell == 1:
            paint_percolation_hexagon(self, percolation, color_lst)
        elif idx_cell == 2:
            paint_percolation_triangle(self, percolation, color_lst)
        elif idx_cell == 3:
            paint_percolation_circle(self, percolation, color_lst)
        elif idx_cell == 4:
            paint_percolation_random_point(self, percolation, color_lst)