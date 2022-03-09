from PIL import Image
import os
import sys
from Application import Converter
from PyQt5.QtWidgets import QApplication, QFileDialog

# print(dir(Converter))
app = QApplication([])
app.setStyleSheet('''
*{

    background-color: #111111;
    color : white;
    font-size : 18px;
}
QLabel{
    font-size : 13px;
}
QListView{
    background-color : #222222;
    font-size : 13px;
}
QListView::item:active{
    background-color : #222222;
    font-size : 13px;
    color : white;
}
QListView::item:!active{
    color : white;
}
QListView::indicator:checked{

    background : green;

}
QListView::indicator:!checked{

    background : #222222;

}
QListView::indicator:unchecked:hover{

    background : white;
}
QListView::indicator:hover{
    background : darkgreen;
}

QLineEdit { 
    background-color: #222222;
    border : none;

}
QPushButton { 
    padding : 15px;
    border : none;    
    background: qlineargradient( x1:0 y1:0.2, x2:1.0 y2:1, stop:0 #555555, stop:1 #333333);
    color : white;
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
my_widget = Converter("Converter")

app.exec_()

sys.exit(0)
