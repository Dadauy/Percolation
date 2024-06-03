from PyQt5.QtGui import QPainter, QColor, QFont, QPen
from PyQt5.QtCore import QPointF, Qt

from paint_percolations.cell import paint_percolation_cell
from paint_percolations.circle import paint_percolation_circle
from paint_percolations.hexagon import paint_percolation_hexagon
from paint_percolations.point import paint_percolation_random_point
from paint_percolations.triangle import paint_percolation_triangle


class PainterPercolation(QPainter):
    def __init__(self, parent=None):
        super(PainterPercolation, self).__init__(parent)

    def paint_first_board(self):
        self.setBrush(QColor(0, 0, 0))
        self.drawRect(350, 20, 920, 880)

    def paint_second_board(self):
        self.drawLine(400, 50, 400, 900)
        self.drawLine(400, 50, 1250, 50)
        self.drawLine(1250, 50, 1250, 900)
        self.drawLine(400, 900, 1250, 900)

    def paint_percolation(self, percolation, color_lst, idx_cell):
        if idx_cell == 0:
            paint_percolation_cell(self, percolation, color_lst)
        elif idx_cell == 1:
            paint_percolation_hexagon(self, percolation, color_lst)
        elif idx_cell == 2:
            paint_percolation_triangle(self, percolation, color_lst)
        elif idx_cell == 3:
            paint_percolation_circle(self, percolation)
        elif idx_cell == 4:
            paint_percolation_random_point(self, percolation, color_lst)

    def paint_info_claster(self, color_claster, cnt_v, center_mass, radius_claster):
        r, g, b = color_claster
        self.setPen(QColor(0, 0, 0))
        self.setBrush(QColor(r, g, b))
        self.drawEllipse(1550, 500, 50, 50)
        self.setFont(QFont('Times New Roman', 20))
        self.drawText(1550, 600, f"{cnt_v}")
        self.drawText(1550, 650, f"{round(center_mass[0], 2), round(center_mass[1], 2)}")
        self.drawText(1550, 700, f"{round(radius_claster, 5)}")

    def paint_radius_claster(self, percolation, center_mass, radius_claster, idx_cell):
        if idx_cell == 0:
            start_x = 400
            start_y = 60
            radius = 800 / (2 * percolation.size - 1)
            self.setBrush(QColor(0, 0, 0, 0))
            self.setPen(QPen(QColor(0, 255, 255), 5))
            self.drawEllipse(
                QPointF(start_x + 2 * (center_mass[0]) * radius + radius / 2,
                        start_y + 2 * (percolation.size - center_mass[1] - 1) * radius + radius / 2),
                2 * radius * radius_claster,
                2 * radius * radius_claster)
        elif idx_cell == 1:
            start_x = 400
            start_y = 60
            radius = 800 / percolation.size_v / 2
            distance = 700 / (2 + (3 / 2) * (percolation.size - 1) + ((1 / 2) if 2 <= percolation.size <= 6 else 0))
            distance_h = distance * ((3 ** (1 / 2)) / 2)
            self.setBrush(QColor(0, 0, 0, 0))
            self.setPen(QPen(QColor(0, 255, 255), 5))
            j = center_mass[0]
            i = (percolation.size_v - center_mass[1] - 1)
            print(j, i)
            add_line = 0
            if int(i) % 2 == 0:
                add_line = (distance / 2) * (i - int(i))
            else:
                add_line = (distance / 2) + distance * (i - int(i))
            self.drawEllipse(QPointF(start_x + j * distance_h + radius / 2,
                                     start_y + 1.5 * (int(i) // 2) * distance + add_line + radius / 2),
                             radius_claster * distance,
                             radius_claster * distance)
