from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from widgets.checkbox_widget import CheckBoxWidget

class OptionsDialog(QDialog) :

    def __init__(self, parent = None) -> None:
        super(OptionsDialog, self).__init__(parent)
        self.setWindowTitle("Options")
        self.setFixedSize(600,650)
        
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowModality(Qt.ApplicationModal)
        
        self.initUI()


    def initUI(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        option1 = CheckBoxWidget("houah !!!", self)
        layout.addWidget(option1)


        self.setLayout(layout)

        self.show()
        pass