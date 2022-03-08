from PIL import Image
import os
import sys

from PyQt5.QtWidgets import QApplication ,QFileDialog

app = QApplication([])
# label = QLabel("Hello there !")
# label.show()
selected_folder = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
print(selected_folder)
# app.exec_()

# sys.exit(0)

# folder_selected = filedialog.askdirectory()

# print(dir(Image))

pictures_folder = selected_folder


files = os.listdir(os.path.join(pictures_folder))
print(files)
for file_name in files:

    full_path = os.path.join(pictures_folder, file_name)
    # print( os.path.isdir(full_path),full_path)
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

    