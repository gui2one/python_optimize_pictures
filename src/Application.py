from fileinput import filename
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
from PyQt5.QtCore import *
from picture_converter import listFilesInDir, optimizePicture
class Converter(QWidget) :

    pictureDir = ""
    label = None
    btn_dir = None
    btn_optimize = None
    list_view = None
    list_view_model = None
    max_size_input = None
    progress = None
    main_frame = None

    def __init__(self, name):
        super().__init__()
        self.initUI()

  

    def initUI(self):
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('SprayLoc -- Picture Optimizer v0.0.1')
        self.setWindowIcon(QIcon('favicon.ico'))

        self.main_frame = QFrame(self)
        # frame.setFrameShape(QFrame.Box)
        layout = QVBoxLayout(self)
        self.main_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.main_frame.setFixedSize(self.size() )
        
        layout.setObjectName("main_layout")
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

        size_input = QInputDialog()
        
        self.list_view = QListWidget()
        self.list_view.setMaximumHeight(250)
        self.list_view.itemClicked.connect(self.onListItemClick)
        sources_layout.addWidget(self.list_view)

        hbox = QHBoxLayout()
        hbox.setAlignment(Qt.AlignLeft)
        layout.addLayout(hbox)

        self.max_size_input = QLineEdit(self)
        self.max_size_input.setText("1640")
        self.max_size_input.setMaximumWidth(100)
        self.max_size_input.editingFinished.connect(self.validateSize)
        hbox.addWidget(self.max_size_input)
        
        label = QLabel(" : Maximum Size entre 250 et 1920.")
        # label.setMaximumWidth(100)
        label.setMaximumHeight(20)
        hbox.addWidget(label)

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
        self.progress.setValue(0)
        for file_name in files :

            item = QListWidgetItem()
            item.setText(file_name)
            item.setCheckState(Qt.Checked)
                  
            self.list_view.addItem(item)


    def optimizePictures(self):

        num_pictures = self.list_view.count()
        for i in range(num_pictures):
            
            item = self.list_view.item(i)
            if item.checkState() :
                print(item.text())
                optimizePicture(item.text(), self.pictureDir, int(self.max_size_input.text()))

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

    def validateSize(self):
        rule = QDoubleValidator(250, 1920, 0)

        
        if rule.validate(self.max_size_input.text(), 42)[0] == QValidator.Acceptable:
            pass
        else :
            # print("not acceptable")
            self.max_size_input.setText("1640")

    def onListItemClick(self, item):
        if item.checkState() ==  Qt.Checked : item.setCheckState(Qt.Unchecked)
        else : item.setCheckState(Qt.Checked)
        # print(item.checkState())