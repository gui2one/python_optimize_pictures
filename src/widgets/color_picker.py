from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class ColorPickerWidget(QWidget):
    

    clicked = pyqtSignal()
    accepted = pyqtSignal()
    def __init__(self, parent = None, initial_color = QColor("white")):
        super(ColorPickerWidget, self).__init__(parent)

        self.setFixedSize(50,25)
        self.color = initial_color
        self.clr_dialog = QColorDialog()
        self.clr_dialog.accepted.connect(self.onAcceptColor)
        
    def paintEvent(self, event):
        
        painter = QPainter(self)
        painter.fillRect(event.rect(), self.color)

    def mousePressEvent(self, ev):

        _color = self.clr_dialog.getColor(self.color)
        self.color = _color
        self.clicked.emit()

    def value(self) -> QColor : 
        
        return self.color
    
    def onAcceptColor(self):
        
        self.accepted.emit()
        print("accept")

 
