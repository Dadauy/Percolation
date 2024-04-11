from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QColor


def paint_percolation_cell(painter, percolation, color_lst):
    start_x = 400
    start_y = 60
    radius = 800 / (2 * percolation.size - 1)
    for i in range(1, percolation.size + 1):
        for j in range(1, percolation.size + 1):
            if percolation.a[i][j] == 0:
                painter.setBrush(QColor(255, 255, 255))
                painter.drawEllipse(
                    QPointF(start_x + 2 * (j - 1) * radius + radius / 2, start_y + 2 * (i - 1) * radius + radius / 2),
                    radius / 2, radius / 2)
            else:
                r, g, b = color_lst[percolation.a[i][j]]
                painter.setBrush(QColor(r, g, b))
                painter.drawEllipse(
                    QPointF(start_x + 2 * (j - 1) * radius + radius / 2, start_y + 2 * (i - 1) * radius + radius / 2),
                    radius / 2, radius / 2)
                if percolation.a[i - 1][j] == percolation.a[i][j] and i != 1:
                    painter.drawLine(QPointF(start_x + 2 * (j - 1) * radius + radius // 2,
                                             start_y + 2 * (i - 1) * radius),
                                     QPointF(start_x + 2 * (j - 1) * radius + radius // 2,
                                             start_y + 2 * (i - 1) * radius - radius))
                if percolation.a[i][j - 1] == percolation.a[i][j] and j != 1:
                    painter.drawLine(QPointF(start_x + 2 * (j - 1) * radius,
                                             start_y + 2 * (i - 1) * radius + radius // 2),
                                     QPointF(start_x + 2 * (j - 1) * radius - radius,
                                             start_y + 2 * (i - 1) * radius + radius // 2))
