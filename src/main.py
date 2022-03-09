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

QListWidget{
    background-color : #222222;
    font-size : 13px;
}
QListWidget::indicator:checked{

    background : green;
    color : white;
    subcontrol-position: top center;
    border : 1px solid white;
}
QListWidget::indicator:unchecked:hover{

    background : white;
}
QListWidget::indicator:hover{
    background : darkgreen;
}

QLineEdit { 
    background-color: #222222;
    border : none;

}
QPushButton { 
    padding : 15px;
    border : none;    
    background-color : #222222;
    color : white;
}

''');
my_widget = Converter("Converter")

app.exec_()

sys.exit(0)
selected_folder = str(QFileDialog.getExistingDirectory(None, "Select Directory"))

pictures_folder = selected_folder


files = os.listdir(os.path.join(pictures_folder))
print(files)
for file_name in files:

    full_path = os.path.join(pictures_folder, file_name)
    if not os.path.isdir(full_path):
        print("\nConverting -> "+file_name)
        with Image.open(os.path.join(pictures_folder, file_name), 'r') as img :


            width = img.size[0]
            height = img.size[1]

            scale_ratio = 1.0
            limit  = 256
            max_dim = max(width, height)
            if  max_dim > limit :
                scale_ratio = limit / max_dim
            new_width =  int(width * scale_ratio)
            new_height =  int(height * scale_ratio)
            # num_components = img.info()
            
            print("\tmode : %s"%(img.mode))
            print("\tformat : %s"%(img.format_description))
            print("\tsize : %d %d"%(width, height))
            print("\tNew size : %d %d"%(new_width, new_height))

            root, ext = os.path.splitext(file_name)
            img.load()
            img = img.resize(size=(new_width, new_height))
            # img.show()

            optim_folder = os.path.join(pictures_folder, "OPTIM")
            if not os.path.isdir(optim_folder):
                os.makedirs(optim_folder, mode=0o700)
            save_path = os.path.join(optim_folder,root+"_OPTIM"+ext)
            
            if ext.lower() == ".jpg" or ext.lower() == ".jpeg":
                img.save(save_path, quality=50)
            else :
                img.save(save_path)

            print("\tSaving to : "+os.path.abspath(save_path))

            img.close()

    