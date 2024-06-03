from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QColor


def paint_percolation_circle(painter, percolation):
    start_x = 400
    start_y = 60

    for circle in percolation.a:
        if circle.color == percolation.color:
            painter.setBrush(QColor(50, 205, 50))
            painter.drawEllipse(QPointF(start_x + circle.x, start_y + circle.y),
                                percolation.size, percolation.size)
        else:
            painter.setBrush(QColor(255, 0, 00))
            painter.drawEllipse(QPointF(start_x + circle.x, start_y + circle.y),
                                percolation.size, percolation.size)

    # TODO: надо пофиксить отображение цвета окна при нажатии сгенерировать
    painter.setBrush(QColor(240, 240, 240))
    painter.setPen(QColor(240, 240, 240))
    painter.drawRect(0, 0, 400, 1024)
    painter.drawRect(0, 0, 1650, 50)
    painter.drawRect(1250, 0, 450, 1024)
    painter.drawRect(0, 900, 1650, 1024)
    painter.setPen(QColor(0, 0, 0))
    painter.drawLine(400, 50, 400, 900)
    painter.drawLine(400, 50, 1250, 50)
    painter.drawLine(1250, 50, 1250, 900)
    painter.drawLine(400, 900, 1250, 900)
