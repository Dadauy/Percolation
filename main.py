import sys
import traceback

from PyQt5.QtGui import QPainter, QColor, QFont, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow

from modeling import WindowModeling
from analiz import WindowAnaliz
from widget_main.push_button import ButtonViewAnaliz, ButtonViewModel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1920, 1080)
        self.move(0, 0)
        self.setWindowTitle("Перколяций")
        self.setWindowIcon(QIcon('_63ce91aa-c753-4226-add5-be6d55d1b340.jpg'))
        # инициализация других окон
        self.WindowAnaliz = WindowAnaliz(self)
        self.WindowModeling = WindowModeling(self)
        self.WindowModeling.setVisible(False)
        self.WindowAnaliz.setVisible(False)
        # инициализация кнопок
        self.ButtonModel = ButtonViewModel(self)
        self.ButtonAnaliz = ButtonViewAnaliz(self)
        self.ButtonModel.clicked.connect(lambda: self.ButtonModel.view_model(self))
        self.ButtonAnaliz.clicked.connect(lambda: self.ButtonAnaliz.view_analiz(self))


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("Oбнаружена ошибка !:", tb)


sys.excepthook = excepthook

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
