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
                            painter.drawLine(QPointF(start_x + (j - 1) * distance_h + (radius / 6),
                                                     start_y + (i - 1 - i // 4) * distance + (radius * 0.130)),
                                             QPointF(start_x + (j - 1) * distance_h + radius / 2 - distance_h + (
                                                     0.340 * radius),
                                                     start_y + (i - 1 - i // 4) * distance - distance / 2 + (
                                                             radius * 0.860)))

                        if percolation.a[i - 1][j + 1] == percolation.a[i][j]:
                            painter.drawLine(QPointF(start_x + (j - 1) * distance_h + (radius / 1.220),
                                                     start_y + (i - 1 - i // 4) * distance + (radius * 0.130)),
                                             QPointF(start_x + (j - 1) * distance_h + radius / 2 + distance_h - (
                                                     0.340 * radius),
                                                     start_y + (i - 1 - i // 4) * distance - distance / 2 + (
                                                             radius * 0.860)))
                elif (j - 1) % 2 == 0:
                    if (i - 1) % 4 == 1:
                        if percolation.a[i - 1][j - 1] == percolation.a[i][j]:
                            painter.drawLine(QPointF(start_x + (j - 1) * distance_h + radius / 6,
                                                     start_y + (
                                                             i - 1 - i // 4) * distance - distance / 2 + radius * 0.12),
                                             QPointF(start_x + (
                                                     j - 1) * distance_h + radius / 2 - distance_h + 0.340 * radius,
                                                     start_y + (i - 1 - i // 4) * distance - distance + radius * 0.860))
                        if percolation.a[i - 1][j + 1] == percolation.a[i][j]:
                            if (j == (percolation.size_h - 1)) and (i == 2):
                                continue
                            pass
                            painter.drawLine(QPointF(start_x + (j - 1) * distance_h + radius / 1.22,
                                                     start_y + (
                                                             i - 1 - i // 4) * distance - distance / 2 + radius * 0.120),
                                             QPointF(start_x + (
                                                     j - 1) * distance_h + radius / 2 + distance_h - 0.340 * radius,
                                                     start_y + (i - 1 - i // 4) * distance - distance + radius * 0.860))
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


def paint_percolation_circle(painter, percolation, color_lst):
    start_x = 400
    start_y = 60
    for circle in percolation.a:
        r, g, b = color_lst[circle.color - 1]
        painter.setBrush(QColor(r, g, b))
        painter.drawEllipse(QPointF(start_x + circle.x, start_y + circle.y),
                            percolation.size, percolation.size)
    # TODO: надо пофиксить отображение цвета окна при нажатии сгенерировать
    painter.setBrush(QColor(240, 240, 240))
    painter.setPen(QColor(240, 240, 240))
    painter.drawRect(0, 0, 400, 1024)
    painter.drawRect(0, 0, 1650, 50)
    painter.drawRect(1250, 0, 1650, 1024)
    painter.drawRect(0, 900, 1650, 1024)
    painter.setPen(QColor(0, 0, 0))
    painter.drawLine(400, 50, 400, 900)
    painter.drawLine(400, 50, 1250, 50)
    painter.drawLine(1250, 50, 1250, 900)
    painter.drawLine(400, 900, 1250, 900)


def paint_percolation_random_point(painter, percolation, color_lst):
    start_x = 400
    start_y = 60
    painter.drawLine(400, 50, 400, 900)
    painter.drawLine(400, 50, 1250, 50)
    painter.drawLine(1250, 50, 1250, 900)
    painter.drawLine(400, 900, 1250, 900)
    for point in percolation.a:
        for child_point in point.neighbours:
            painter.drawLine(QPointF(start_x + point.x, start_y + point.y),
                             QPointF(start_x + percolation.a[child_point].x, start_y + percolation.a[child_point].y))
        r, g, b = color_lst[point.color - 1]
        painter.setBrush(QColor(r, g, b))
        painter.drawEllipse(QPointF(start_x + point.x, start_y + point.y),
                            5, 5)
