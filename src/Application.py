from fileinput import filename
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem
from PyQt5.QtGui import  QStandardItem
from PyQt5.QtCore import Qt
from picture_converter import listFilesInDir, optimizePicture
class Converter(QWidget) :

    pictureDir = ""
    label = None
    btn_dir = None
    btn_optimize = None
    list_view = None
    list_view_model = None
    progress = None
    def __init__(self, name):
        super().__init__()

        self.initUI()

        # self.pictureDir = ""

    def initUI(self):
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('SprayLoc -- Picture Converter version 0.0.1')
        # self.setWindowIcon(QIcon('web.png'))

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)
        self.btn_dir = QPushButton("Choisir un Dossier", self)
        layout.addWidget(self.btn_dir)
        self.btn_dir.clicked.connect(self.getFolderName)

        sources_layout = QHBoxLayout()
        layout.addLayout(sources_layout)
        btns_layout = QVBoxLayout()
        btns_layout.setAlignment(Qt.AlignTop)
        sources_layout.addLayout(btns_layout)
        select_all_btn = QPushButton("Select all")
        select_all_btn.clicked.connect(self.selectAll)
        btns_layout.addWidget(select_all_btn)
        deselect_all_btn = QPushButton("Deselect all")
        deselect_all_btn.clicked.connect(self.deselectAll)
        btns_layout.addWidget(deselect_all_btn)
        
        self.list_view = QListWidget()
        self.list_view.setMaximumHeight(250)

        sources_layout.addWidget(self.list_view)


        self.btn_optimize = QPushButton("Optimize Pictures", self)
        self.btn_optimize.clicked.connect(self.optimizePictures)
        layout.addWidget(self.btn_optimize)

        self.progress = QProgressBar()
        layout.addWidget(self.progress)
        
        self.show()

    def getFolderName(self): 
        selected_folder = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        if selected_folder.strip(" ") == '' : return
        self.pictureDir = selected_folder
        # print(self.pictureDir)
        self.btn_dir.setText(self.pictureDir)
        files = listFilesInDir(self.pictureDir)

        self.list_view.clear()
        for file_name in files :

            item = QListWidgetItem()
            item.setText(file_name)
            item.setCheckState(Qt.Checked)            

            self.list_view.addItem(item)

    def optimizePictures(self):

        num_pictures = self.list_view.count()
        for i in range(num_pictures):
            
            item = self.list_view.item(i)
            # print(item.getCheckState())
            # print(item.checkState())
            if item.checkState() :
                print(item.text())
                optimizePicture(item.text(), self.pictureDir)

            percent = int(i / (num_pictures-1) * 100)
            self.progress.setValue(percent)

    def selectAll(self):
        for i in range(self.list_view.count()):
            
            item = self.list_view.item(i)
            item.setCheckState(Qt.Checked)

    def deselectAll(self):
        for i in range(self.list_view.count()):
            
            item = self.list_view.item(i)
            item.setCheckState(Qt.Unchecked)