from PyQt5.QtGui import QBrush, QPen, QPainter, QColor, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QLineF, QPointF
from decimal import Decimal


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


def paint_percolation_hexagon(painter, percolation, color_lst):
    start_x = 350
    start_y = 60
    if percolation.size != 0:
        radius = 800 / percolation.size_v / 2
        distance = 700 / (2 + (3 / 2) * (percolation.size - 1))
        distance_h = distance * ((3 ** (1 / 2)) / 2)
    black_set = (
        (percolation.size_v, 1), (percolation.size_v, percolation.size_h), (1, percolation.size_h))
    for i in range(1, percolation.size_v + 1):
        for j in range(1, percolation.size_h + 1):
            if (i, j) in black_set:
                continue
            if percolation.a[i][j]:
                r, g, b = color_lst[percolation.a[i][j]]
                painter.setBrush(QColor(r, g, b))
            else:
                painter.setBrush(QColor(255, 255, 255))
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
                            painter.drawLine(QPointF(start_x + (j - 1) * distance_h + radius / 2,
                                                     start_y + (i - 1 - i // 4) * distance),
                                             QPointF(start_x + (j - 1) * distance_h + radius / 2,
                                                     start_y + (i - 1 - i // 4) * distance - distance + radius))
                    elif (i - 1) % 4 == 3:
                        if percolation.a[i - 1][j - 1] == percolation.a[i][j]:
                            painter.drawLine(QPointF(start_x + (j - 1) * distance_h + radius / 2,
                                                     start_y + (i - 1 - i // 4) * distance),
                                             QPointF(start_x + (j - 1) * distance_h + radius / 2 - distance_h,
                                                     start_y + (i - 1 - i // 4) * distance - distance / 2 + radius))
                        if percolation.a[i - 1][j + 1] == percolation.a[i][j]:
                            painter.drawLine(QPointF(start_x + (j - 1) * distance_h + radius / 2,
                                                     start_y + (i - 1 - i // 4) * distance),
                                             QPointF(start_x + (j - 1) * distance_h + radius / 2 + distance_h,
                                                     start_y + (i - 1 - i // 4) * distance - distance / 2 + radius))
                elif (j - 1) % 2 == 0:
                    if (i - 1) % 4 == 1:
                        if percolation.a[i - 1][j - 1] == percolation.a[i][j]:
                            painter.drawLine(QPointF(start_x + (j - 1) * distance_h + radius / 2,
                                                     start_y + (i - 1 - i // 4) * distance - distance / 2),
                                             QPointF(start_x + (j - 1) * distance_h + radius / 2 - distance_h,
                                                     start_y + (i - 1 - i // 4) * distance - distance + radius))
                        if percolation.a[i - 1][j + 1] == percolation.a[i][j]:
                            if (j == (percolation.size_h - 1)) and (i == 2):
                                continue
                            painter.drawLine(QPointF(start_x + (j - 1) * distance_h + radius / 2,
                                                     start_y + (i - 1 - i // 4) * distance - distance / 2),
                                             QPointF(start_x + (j - 1) * distance_h + radius / 2 + distance_h,
                                                     start_y + (i - 1 - i // 4) * distance - distance + radius))
                    elif (i - 1) % 4 == 2:
                        if percolation.a[i - 1][j] == percolation.a[i][j]:
                            painter.drawLine(QPointF(start_x + (j - 1) * distance_h + radius / 2,
                                                     start_y + (i - 1 - i // 4) * distance - distance / 2),
                                             QPointF(start_x + (j - 1) * distance_h + radius / 2,
                                                     start_y + (
                                                             i - 1 - i // 4) * distance + radius - distance / 2 - distance))


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
                        painter.drawLine(QPointF(start_x + 2 * (j - 1) * radius + radius / 2,
                                                 start_y + 2 * (i - 1) * radius),
                                         QPointF(start_x + 2 * (j - 1) * radius - radius - radius / 2,
                                                 start_y + 2 * (i - 1) * radius - radius))
                    if percolation.a[i - 1][j + 1] == percolation.a[i][j]:
                        painter.drawLine(QPointF(start_x + 2 * (j - 1) * radius + radius / 2,
                                                 start_y + 2 * (i - 1) * radius),
                                         QPointF(start_x + 2 * (j - 1) * radius + 2 * radius + radius / 2,
                                                 start_y + 2 * (i - 1) * radius - radius))
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
