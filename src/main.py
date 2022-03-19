import sys
from Application import Optimizer
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from options_dialog import OptionsDialog
from app_settings import ApplicationSettings
from picture_optimizer import OptimizerOptions
class MainWindow(QMainWindow):

    def __init__(self, parent = None):
        super(MainWindow,self).__init__(parent)

        self.settings = ApplicationSettings()

        
        self.setWindowTitle('SprayLoc -- Picture Optimizer v0.0.3')
        self.setWindowIcon(QIcon('favicon.ico'))
        self.converter_window = Optimizer('Optimizer 2')
        self.setCentralWidget(self.converter_window)
        
        
        option_action = self.menuBar().addAction("Options")
        option_action.triggered.connect(self.displayOptions)
        
        
        self.restoreSettings()
        self.show()

    def displayOptions(self):
        
        options = OptimizerOptions()
        options.background_color = QColor(0,0,0,255)
        # options.background_color.setRed()
        w = OptionsDialog(options, self)
        w.exec()
    
    def saveSettings(self):
        self.settings.setValue("window_position", self.pos())
        self.settings.setValue("window_size", self.size())
        
        self.settings.setValue("directory", self.converter_window.pictureDir)
        
        self.settings.setValue("bg_color_r", int(self.converter_window.options.background_color.red()))
            
        pass
    
    def restoreSettings(self):

        ## apply saved settings

        size : QSize = self.settings.value("window_size")
        pos : QPoint = self.settings.value("window_position")
        if size != None and pos != None :
            self.setGeometry(pos.x(), pos.y()+40, size.width(), size.height())

        
        self.converter_window.pictureDir = self.settings.value("directory")
        self.converter_window.buildFilesList()
        
        try : 
            self.converter_window.options.background_color.setRed(self.settings.value("bg_color_r"))
        except:
            pass
        
    def closeEvent(self, event: QCloseEvent) -> None:
        self.saveSettings()

        return super().closeEvent(event)
    
    
app = QApplication([])

app.setStyleSheet('''
*{

    background-color: #111111;

    font-size : 15px;
}
QMenuBar{
    color : white;
}
QLabel{
    font-size : 13px;
    color : white;
}
QTableView{
    background-color : #222222;
    selection-background-color : #222266;
    color : black;
    font-size : 13px;
}

QTableView::item:active{
    /* background-color : #222222; */
    font-size : 13px;
    color : white;
}
QTableView::item:!active{
    color : white;
}
QTableView::indicator:checked{

    background : green;

}
QTableView::indicator:!checked{

    background : #222222;

}

QTableView::indicator:hover{
    
    border : 2px solid white;
}

QLineEdit { 
    color : white;
    background-color: #222222;
    border : none;

}
QPushButton { 
    padding : 15px;
    border : none;    
    background: qlineargradient( x1:0 y1:0.2, x2:1.0 y2:1, stop:0 #555555, stop:1 #333333);
    color : white;
}
QPushButton:hover{
    border : 1px solid white; 
}
QPushButton#GO { 
    padding : 15px;
    border : none;    
    background: qlineargradient( x1:0 y1:0.2, x2:1.0 y2:1, stop:0 #22aa22, stop:1 #559955);
    color : white;
}
QPushButton#GO:hover { 
    background: qlineargradient( x1:0 y1:0.2, x2:1.0 y2:1, stop:0 #33bb33, stop:1 #559955);
 
}
QPushButton#GO:disabled{
    background: qlineargradient( x1:0 y1:0.2, x2:1.0 y2:1, stop:0 #337733, stop:1 #556655);

}
QProgressBar {
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center;
}

QProgressBar::chunk {
    background-color: #05B8CC;
    width: 20px;
}
''');

window = MainWindow()
app.exec_()

sys.exit(0)
