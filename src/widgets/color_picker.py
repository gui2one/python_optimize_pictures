from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class ColorPickerWidget(QWidget):
    

    clicked = pyqtSignal()
    def __init__(self, parent = None):
        super(ColorPickerWidget, self).__init__(parent)
        # print("ColorPickerWidget")
        self.setFixedSize(50,25)
        self.color = QColor("white")
        
    def paintEvent(self, event):
        print(event)
        painter = QPainter(self)

        painter.fillRect(event.rect(), self.color)

    def mousePressEvent(self, ev):
        w = QColorDialog(self)
        # w.exec()

        _color = w.getColor()
        self.color = _color
        self.clicked.emit()

    def value(self) -> QColor : 
        return self.color