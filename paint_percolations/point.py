from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QColor


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
        painter.drawEllipse(QPointF(start_x + point.x, start_y + point.y), 5, 5)
