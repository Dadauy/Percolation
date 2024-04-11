from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QColor, QPainterPath


def paint_percolation_triangle(painter, percolation, color_lst):
    start_x = 400
    start_y = 60
    radius = 800 / (2 * percolation.size_h - 1)
    for i in range(1, percolation.size_v + 1):
        for j in range(1, percolation.size_h + 1):
            if ((i - 1) % 2 == 0 and (j - 1) % 2 == 1) or ((i - 1) % 2 == 1 and (j - 1) % 2 == 0):
                painter.setPen(QColor(0, 0, 0))
                if percolation.a[i][j]:
                    r, g, b = color_lst[percolation.a[i][j]]
                    painter.setBrush(QColor(r, g, b))
                    painter.drawEllipse(
                        QPointF(start_x + 2 * (j - 1) * radius + radius / 2,
                                start_y + 2 * (i - 1) * radius + radius / 2),
                        radius / 2, radius / 2)
                    if percolation.a[i - 1][j - 1] == percolation.a[i][j]:
                        painter.setPen(QColor(r, g, b))
                        path = QPainterPath(
                            QPointF(start_x + 2 * (j - 1) * radius + 0.15 * radius,
                                    start_y + 2 * (i - 1) * radius + 0.86 * radius))
                        path.lineTo(start_x + 2 * (j - 1) * radius + 0.86 * radius,
                                    start_y + 2 * (i - 1) * radius + 0.16 * radius)
                        path.lineTo(start_x + 2 * (j - 1) * radius - 1.16 * radius,
                                    start_y + 2 * (i - 1) * radius - 1.860 * radius)
                        path.lineTo(start_x + 2 * (j - 1) * radius - 1.850 * radius,
                                    start_y + 2 * (i - 1) * radius - 1.140 * radius)
                        painter.drawPath(path)
                    if percolation.a[i - 1][j + 1] == percolation.a[i][j]:
                        painter.setPen(QColor(r, g, b))
                        path = QPainterPath(
                            QPointF(start_x + 2 * (j - 1) * radius + 0.160 * radius,
                                    start_y + 2 * (i - 1) * radius + 0.140 * radius))
                        path.lineTo(start_x + 2 * (j - 1) * radius + 0.850 * radius,
                                    start_y + 2 * (i - 1) * radius + 0.850 * radius)
                        path.lineTo(start_x + 2 * (j - 1) * radius + 2.860 * radius,
                                    start_y + 2 * (i - 1) * radius - 1.150 * radius)
                        path.lineTo(start_x + 2 * (j - 1) * radius + 2.150 * radius,
                                    start_y + 2 * (i - 1) * radius - 1.850 * radius)
                        painter.drawPath(path)
                    if (j - 2) >= 0 and percolation.a[i][j - 2] == percolation.a[i][j]:
                        painter.setPen(QColor(r, g, b))
                        path = QPainterPath(
                            QPointF(start_x + 2 * (j - 1) * radius + 0.5 * radius,
                                    start_y + 2 * (i - 1) * radius))
                        path.lineTo(start_x + 2 * (j - 1) * radius + 0.5 * radius,
                                    start_y + 2 * (i - 1) * radius + radius)
                        path.lineTo(start_x + 2 * (j - 1) * radius - 3.5 * radius,
                                    start_y + 2 * (i - 1) * radius + radius)
                        path.lineTo(start_x + 2 * (j - 1) * radius - 3.5 * radius,
                                    start_y + 2 * (i - 1) * radius)
                        painter.drawPath(path)
                else:
                    painter.setBrush(QColor(255, 255, 255))
                    painter.drawEllipse(
                        QPointF(start_x + 2 * (j - 1) * radius + radius / 2,
                                start_y + 2 * (i - 1) * radius + radius / 2),
                        radius / 2, radius / 2)
