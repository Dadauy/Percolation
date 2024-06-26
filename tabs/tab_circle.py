from PyQt5.QtWidgets import QTabWidget
from graf_widget.graf import MatplotlibWidget
import numpy


class TabsWidgetCircle(QTabWidget):
    def __init__(self, parent=None):
        super(TabsWidgetCircle, self).__init__(parent)
        self.setGeometry(50, 50, 1450, 900)

        self.show_plot_circle()

    def show_plot_circle(self):
        x_data = numpy.array([i for i in range(30, 500 + 1)])
        y_data = numpy.load("./plots_old/circle4.npy")

        matplotlib_widget = MatplotlibWidget()
        matplotlib_widget.plot_2d(x_data, y_data)
        matplotlib_widget.ax.set_xlabel("Размер кластера")
        matplotlib_widget.ax.set_ylabel("отношение(сумма площадей кругов / размер всей площади)")

        self.addTab(matplotlib_widget, 'Инвариантность')
