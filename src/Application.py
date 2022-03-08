from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QFileDialog, QVBoxLayout, QListView
from PyQt5.QtGui import QIcon

class Converter(QWidget) :

    pictureDir = ""
    label = None
    btn_dir = None
    list_view = None
    def __init__(self, name):
        super().__init__()

        self.initUI()

        self.pictureDir = ""

    def initUI(self):
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('SprayLoc -- Picture Converter version 0.0.1')
        # self.setWindowIcon(QIcon('web.png'))

        layout = QVBoxLayout(self)
        self.btn_dir = QPushButton("Choisir un Dossier", self)
        layout.addWidget(self.btn_dir)
        self.btn_dir.clicked.connect(self.getFolderName)

        self.list_view = QListView()
        layout.addWidget(self.list_view)
        
        self.show()

    def getFolderName(self): 
        selected_folder = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        self.pictureDir = selected_folder
        print(self.pictureDir)
        self.btn_dir.setText(self.pictureDir)
