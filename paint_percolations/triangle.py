from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QColor


def paint_percolation_triangle(painter, percolation, color_lst):
    start_x = 400
    start_y = 60
    radius = 800 / (2 * percolation.size_h - 1)
    for i in range(1, percolation.size_v + 1):
        for j in range(1, percolation.size_h + 1):
            if ((i - 1) % 2 == 0 and (j - 1) % 2 == 1) or ((i - 1) % 2 == 1 and (j - 1) % 2 == 0):
                if percolation.a[i][j]:
                    r, g, b = color_lst[percolation.a[i][j]]
                    painter.setBrush(QColor(r, g, b))
                    painter.drawEllipse(
                        QPointF(start_x + 2 * (j - 1) * radius + radius / 2,
                                start_y + 2 * (i - 1) * radius + radius / 2),
                        radius / 2, radius / 2)
                    if percolation.a[i - 1][j - 1] == percolation.a[i][j]:
                        painter.drawLine(QPointF(start_x + 2 * (j - 1) * radius + radius / 6,
                                                 start_y + 2 * (i - 1) * radius + radius * 0.130),
                                         QPointF(start_x + 2 * (j - 1) * radius - radius / 2 - 0.640 * radius,
                                                 start_y + 2 * (i - 1) * radius - 1.140 * radius))
                    if percolation.a[i - 1][j + 1] == percolation.a[i][j]:
                        painter.drawLine(QPointF(start_x + 2 * (j - 1) * radius + radius / 1.220,
                                                 start_y + 2 * (i - 1) * radius + 0.130 * radius),
                                         QPointF(start_x + 2 * (j - 1) * radius + radius / 2 + 1.640 * radius,
                                                 start_y + 2 * (i - 1) * radius - 1.140 * radius))
                    if (j - 2) >= 0 and percolation.a[i][j - 2] == percolation.a[i][j]:
                        painter.drawLine(QPointF(start_x + 2 * (j - 1) * radius,
                                                 start_y + 2 * (i - 1) * radius + radius / 2),
                                         QPointF(start_x + 2 * (j - 1) * radius - 3 * radius,
                                                 start_y + 2 * (i - 1) * radius + radius / 2))
                else:
                    painter.setBrush(QColor(255, 255, 255))
                    painter.drawEllipse(
                        QPointF(start_x + 2 * (j - 1) * radius + radius / 2,
                                start_y + 2 * (i - 1) * radius + radius / 2),
                        radius / 2, radius / 2)
