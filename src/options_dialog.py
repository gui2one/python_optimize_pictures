from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from widgets.checkbox_widget import CheckBoxWidget
from widgets.color_picker import ColorPickerWidget

from picture_optimizer import OptimizerOptions 

class OptionsDialog(QDialog) :

    def __init__(self, options : OptimizerOptions, parent = None):
        super(OptionsDialog, self).__init__(parent)
        self.options = options 
        self.setWindowTitle("Options")
        self.setFixedSize(500,500)
        self.setWindowModality(Qt.ApplicationModal)
        
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        option1 = CheckBoxWidget("Convert PNGs to JPEG", self)
        layout.addWidget(option1)


        self.color_option = ColorPickerWidget(self)
        

        layout.addWidget(self.color_option)

        self.setLayout(layout)
        
        
    def closeEvent(self, event: QCloseEvent):
        self.options.background_colo = self.color_option.value()
        
        print(self.options)
        return super().closeEvent(event)