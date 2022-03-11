from zipfile import ZipFile
import os
from os.path import basename

# create a ZipFile object
with ZipFile('archive.zip', 'w') as zipObj:
   # Iterate over all the files in directory
   for folderName, subfolders, filenames in os.walk('dist'):
       for filename in filenames:
           #create complete filepath of file in directory
           filePath = os.path.join(folderName, filename)
           # Add file to zip
           print(filePath)
           
           zipObj.write(filePath, os.path.join("SpraLoc-Picture-Optimizer", filename))