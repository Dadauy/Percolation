from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QColor


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
