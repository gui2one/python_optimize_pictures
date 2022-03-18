from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from widgets.checkbox_widget import CheckBoxWidget
from widgets.color_picker import ColorPickerWidget

class OptionsDialog(QDialog) :

    def __init__(self, parent = None):
        super(OptionsDialog, self).__init__(parent)
        self.setWindowTitle("Options")
        self.setFixedSize(500,500)
        self.setWindowModality(Qt.ApplicationModal)
        
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        option1 = CheckBoxWidget("Convert PNGs to JPEG", self)
        layout.addWidget(option1)


        color_option = ColorPickerWidget(self)
        # color_option.update()

        layout.addWidget(color_option)

        self.setLayout(layout)