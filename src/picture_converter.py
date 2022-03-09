from PIL import Image
import os

def checkImageExtension(file_name) :
    extension_list = [".webp",".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif", ".gif"]
    root , ext = os.path.splitext(file_name)
    if ext.lower() in extension_list:
        return True

    return False

def listFilesInDir( dir_path):
    files = os.listdir(os.path.join(dir_path))
    
    clean_files = []
    for item in files :
        if not os.path.isdir(os.path.join(dir_path, item)):
            if checkImageExtension(item):
                clean_files.append(item)
    return clean_files

def optimizePicture(file_name, pictures_folder, max_size=512):
    with Image.open(os.path.join(pictures_folder, file_name), 'r') as img :


        width = img.size[0]
        height = img.size[1]

        scale_ratio = 1.0
        limit  = max_size
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