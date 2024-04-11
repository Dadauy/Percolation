from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QColor, QPainterPath


def paint_percolation_hexagon(painter, percolation, color_lst):
    start_x = 400
    start_y = 60
    if percolation.size != 0:
        radius = 800 / percolation.size_v / 2
        distance = 700 / (2 + (3 / 2) * (percolation.size - 1) + ((1 / 2) if 2 <= percolation.size <= 6 else 0))
        distance_h = distance * ((3 ** (1 / 2)) / 2)
    black_set = (
        (percolation.size_v, 1), (percolation.size_v, percolation.size_h), (1, percolation.size_h))

    for i in range(1, percolation.size_v + 1):
        for j in range(1, percolation.size_h + 1):
            if (i, j) in black_set:
                continue
            painter.setBrush(QColor(255, 255, 255))
            painter.setPen(QColor(0, 0, 0))
            if percolation.a[i][j]:
                r, g, b = color_lst[percolation.a[i][j]]
                painter.setBrush(QColor(r, g, b))
                painter.setPen(QColor(r, g, b))
            if (j - 1) % 2 == 1:
                if (i - 1) % 4 == 0:
                    painter.drawEllipse(QPointF(start_x + (j - 1) * distance_h + radius / 2,
                                                start_y + (i - 1 - i // 4) * distance + radius / 2),
                                        radius / 2,
                                        radius / 2)
                elif (i - 1) % 4 == 3:
                    painter.drawEllipse(QPointF(start_x + (j - 1) * distance_h + radius / 2,
                                                start_y + (i - 1 - i // 4) * distance + radius / 2),
                                        radius / 2,
                                        radius / 2)
            elif (j - 1) % 2 == 0:
                if (i - 1) % 4 == 1:
                    painter.drawEllipse(QPointF(start_x + (j - 1) * distance_h + radius / 2,
                                                start_y + (i - 1 - i // 4) * distance + radius / 2 - distance / 2),
                                        radius / 2,
                                        radius / 2)
                elif (i - 1) % 4 == 2:
                    painter.drawEllipse(QPointF(start_x + (j - 1) * distance_h + radius / 2,
                                                start_y + (i - 1 - i // 4) * distance + radius / 2 - distance / 2),
                                        radius / 2,
                                        radius / 2)
            if percolation.a[i][j]:
                if (j - 1) % 2 == 1:
                    if (i - 1) % 4 == 0:
                        if percolation.a[i - 1][j] == percolation.a[i][j]:
                            path = QPainterPath(
                                QPointF(start_x + (j - 1) * distance_h,
                                        start_y + (i - 1 - i // 4) * distance + radius / 2))
                            path.lineTo(start_x + (j - 1) * distance_h + radius,
                                        start_y + (i - 1 - i // 4) * distance + radius / 2)
                            path.lineTo(start_x + (j - 1) * distance_h + radius,
                                        start_y + (i - 1 - i // 4) * distance + radius / 2 - distance)
                            path.lineTo(start_x + (j - 1) * distance_h,
                                        start_y + (i - 1 - i // 4) * distance + radius / 2 - distance)
                            painter.drawPath(path)
                    elif (i - 1) % 4 == 3:
                        if percolation.a[i - 1][j - 1] == percolation.a[i][j]:
                            path = QPainterPath(
                                QPointF(start_x + (j - 1) * distance_h + 0.350 * radius,
                                        start_y + (i - 1 - i // 4) * distance + 0.985 * radius))
                            path.lineTo(start_x + (j - 1) * distance_h + 0.800 * radius,
                                        start_y + (i - 1 - i // 4) * distance + 0.100 * radius)
                            path.lineTo(start_x + (j - 1) * distance_h + radius / 2 - distance_h + 0.125 * radius,
                                        start_y + (i - 1 - i // 4) * distance - distance / 2 + 0.005 * radius)
                            path.lineTo(start_x + (j - 1) * distance_h + radius / 2 - distance_h - 0.160 * radius,
                                        start_y + (i - 1 - i // 4) * distance - distance / 2 + 0.980 * radius)
                            painter.drawPath(path)
                        if percolation.a[i - 1][j + 1] == percolation.a[i][j]:
                            path = QPainterPath(
                                QPointF(start_x + (j - 1) * distance_h + 0.800 * radius,
                                        start_y + (i - 1 - i // 4) * distance + 0.915 * radius))
                            path.lineTo(start_x + (j - 1) * distance_h + 0.260 * radius,
                                        start_y + (i - 1 - i // 4) * distance + 0.060 * radius)
                            path.lineTo(start_x + (j - 1) * distance_h + radius / 2 + distance_h - 0.230 * radius,
                                        start_y + (i - 1 - i // 4) * distance - distance / 2 + 0.05 * radius)
                            path.lineTo(start_x + (j - 1) * distance_h + radius / 2 + distance_h + 0.260 * radius,
                                        start_y + (i - 1 - i // 4) * distance - distance / 2 + 0.94 * radius)
                            painter.drawPath(path)
                elif (j - 1) % 2 == 0:
                    if (i - 1) % 4 == 1:
                        if percolation.a[i - 1][j - 1] == percolation.a[i][j]:
                            path = QPainterPath(
                                QPointF(start_x + (j - 1) * distance_h + 0.350 * radius,
                                        start_y + (i - 1 - i // 4) * distance - distance / 2 + 0.985 * radius))
                            path.lineTo(start_x + (j - 1) * distance_h + 0.800 * radius,
                                        start_y + (i - 1 - i // 4) * distance - distance / 2 + 0.100 * radius)
                            path.lineTo(start_x + (j - 1) * distance_h + radius / 2 - distance_h + 0.125 * radius,
                                        start_y + (i - 1 - i // 4) * distance - distance + 0.005 * radius)
                            path.lineTo(start_x + (j - 1) * distance_h + radius / 2 - distance_h - 0.160 * radius,
                                        start_y + (i - 1 - i // 4) * distance - distance + 0.980 * radius)
                            painter.drawPath(path)
                        if percolation.a[i - 1][j + 1] == percolation.a[i][j]:
                            if (j == (percolation.size_h - 1)) and (i == 2):
                                continue
                            path = QPainterPath(
                                QPointF(start_x + (j - 1) * distance_h + 0.740 * radius,
                                        start_y + (i - 1 - i // 4) * distance - distance / 2 + 0.960 * radius))
                            path.lineTo(start_x + (j - 1) * distance_h + 0.240 * radius,
                                        start_y + (i - 1 - i // 4) * distance - distance / 2 + 0.070 * radius)
                            path.lineTo(start_x + (j - 1) * distance_h + radius / 2 + distance_h - 0.140 * radius,
                                        start_y + (i - 1 - i // 4) * distance - distance + 0.010 * radius)
                            path.lineTo(start_x + (j - 1) * distance_h + radius / 2 + distance_h + 0.260 * radius,
                                        start_y + (i - 1 - i // 4) * distance - distance + 0.94 * radius)
                            painter.drawPath(path)
                    elif (i - 1) % 4 == 2:
                        if percolation.a[i - 1][j] == percolation.a[i][j]:
                            path = QPainterPath(
                                QPointF(start_x + (j - 1) * distance_h,
                                        start_y + (i - 1 - i // 4) * distance - distance / 2 + radius / 2))
                            path.lineTo(start_x + (j - 1) * distance_h + radius,
                                        start_y + (i - 1 - i // 4) * distance - distance / 2 + radius / 2)
                            path.lineTo(start_x + (j - 1) * distance_h + radius,
                                        start_y + (i - 1 - i // 4) * distance + radius / 2 - (3 / 2) * distance)
                            path.lineTo(start_x + (j - 1) * distance_h,
                                        start_y + (i - 1 - i // 4) * distance + radius / 2 - (3 / 2) * distance)
                            painter.drawPath(path)
