from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from widgets.checkbox_widget import CheckBoxWidget
from widgets.color_picker import ColorPickerWidget

from picture_optimizer import OptimizerOptions 

class OptionsDialog(QDialog) :

    def __init__(self,parent = None):
        super(OptionsDialog, self).__init__(parent)
        
        self.setWindowTitle("Options")
        self.setFixedSize(500,500)
        self.setWindowModality(Qt.ApplicationModal)
        self.options : OptimizerOptions = self.parent().converter_window.options
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        self.option1 = CheckBoxWidget("Convert PNGs to JPEG", self)
        self.option1.setValue(self.options.b_convert_png_to_jpeg)
        layout.addWidget(self.option1)


        self.color_option = ColorPickerWidget(self, self.options.background_color)
        

        layout.addWidget(self.color_option)

        self.setLayout(layout)
        
        
    def closeEvent(self, event: QCloseEvent):
        self.options.background_color = self.color_option.value()
        self.options.b_convert_png_to_jpeg = self.option1.value() == Qt.Checked
        return super().closeEvent(event)