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
    for file_name in files :
        path_to_file = os.path.join(dir_path, file_name)
        if not os.path.isdir(path_to_file):
            if checkImageExtension(file_name):
                size = os.path.getsize(path_to_file)
                clean_files.append((file_name, size))
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
        # img = img.convert('RGB')


        # img = img.convert('P', palette=Image.ADAPTIVE)
        optim_folder = os.path.join(pictures_folder, "OPTIM")
        if not os.path.isdir(optim_folder):
            os.makedirs(optim_folder, mode=0o700)
        
        # if ext.lower() == ".png"  or ext.lower() == ".webp":
        #     img = img.convert('RGB')
        #     ext = ".jpg" 

        save_path = os.path.join(optim_folder,root+"_OPTIM"+ext)
        if ext.lower() == ".jpg" or ext.lower() == ".jpeg":
            img.save(save_path, quality=50)
        else :
            img.save(save_path)

        print("\tSaving to : "+os.path.abspath(save_path))

        img.close()

        return os.path.abspath(save_path)
    
    return None