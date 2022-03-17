from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class OptionsDialog(QDialog) :

    def __init__(self, parent = None) -> None:
        super(OptionsDialog, self).__init__(parent)
        self.setWindowTitle("Options")
        self.setFixedSize(600,650)
        
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowModality(Qt.ApplicationModal)