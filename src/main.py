import sys
from Application import Converter
from PyQt5.QtWidgets import QApplication


app = QApplication([])
app.setStyleSheet('''
*{

    background-color: #111111;

    font-size : 15px;
}
QLabel{
    font-size : 13px;
    color : white;
}
QTableView{
    background-color : #222222;
    selection-background-color : #222222;
    color : black;
    font-size : 13px;
}
QTableView QTableCornerButton::section {
    background: white;
    border: 2px outset red;
}
QTableView::item:active{
    background-color : #222222;
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
