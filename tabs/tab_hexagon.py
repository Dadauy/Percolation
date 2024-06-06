import numpy
from PyQt5.QtWidgets import QTabWidget
from graf_widget.graf import MatplotlibWidget, Matplotlib3DWidget


class TabsWidgetHexagon(QTabWidget):
    def __init__(self, parent=None):
        super(TabsWidgetHexagon, self).__init__(parent)
        self.setGeometry(50, 50, 1450, 900)

        self.show_g()

    def show_g(self):
        a = numpy.array([i / 100 for i in range(101)])
        b = numpy.array([i for i in range(1, 30)])
        a, b = numpy.meshgrid(a, b)
        c = numpy.load("./plots/hexagon_probably.npy")

        m = Matplotlib3DWidget()
        m.plot_3d(a, b, c)
        m.ax.set_xlabel('Вероятность узла')
        m.ax.set_ylabel('Размер решетки')
        m.ax.set_zlabel('Шанс появления кластера')

        self.addTab(m, "Шанс появления")
