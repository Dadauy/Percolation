from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider


class SliderSize(QSlider):
    def __init__(self, parent=None):
        super(SliderSize, self).__init__(parent)
        self.setGeometry(0, 0, 300, 50)
        self.move(1550, 200)
        self.setOrientation(Qt.Horizontal)
        self.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.setRange(0, 100)
        self.setSingleStep(5)
        self.valueChanged.connect(lambda: self.update_value_size(parent))

    def update_value_size(self, parent):
        parent.label_size.setText(f"N: {self.value()}")


class SliderProbability(QSlider):
    def __init__(self, parent=None):
        super(SliderProbability, self).__init__(parent)
        self.setGeometry(0, 0, 300, 50)
        self.move(1550, 300)
        self.setOrientation(Qt.Horizontal)
        self.setRange(0, 1000)
        self.setSingleStep(50)
        self.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.valueChanged.connect(lambda: self.update_value_probability(parent))

    def update_value_probability(self, parent):
        parent.label_probability.setText(f"P: {self.value() / 1000:.3f}")


class SliderSizeCircle(QSlider):
    def __init__(self, parent=None):
        super(SliderSizeCircle, self).__init__(parent)
        self.setGeometry(0, 0, 300, 50)
        self.move(1550, 300)
        self.setOrientation(Qt.Horizontal)
        self.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.setRange(30, 400)
        self.setSingleStep(5)
        self.valueChanged.connect(lambda: self.update_value_size(parent))

    def update_value_size(self, parent):
        parent.label_size_circle.setText(f"R: {self.value()}")
