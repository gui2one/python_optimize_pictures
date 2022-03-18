from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class CheckBoxWidget(QWidget):
    def __init__(self, label : str,  parent = None):
        super(CheckBoxWidget, self).__init__(parent)

        layout = QHBoxLayout()
        
        self.check_box = QCheckBox(self)
        layout.addWidget(self.check_box)    
        
        self.label = ClickableLabel(label)
        self.label.clicked.connect(lambda : self.check_box.toggle())
        layout.addWidget(self.label)

        self.setLayout(layout)


class ClickableLabel(QLabel):

    clicked=pyqtSignal()

    def mousePressEvent(self, ev):
        self.clicked.emit()