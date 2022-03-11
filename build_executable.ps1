Remove-Item -Path "./dist/SprayLoc_Pic_Optimizer.exe"
pyinstaller --icon=./favicon.ico --onefile --noconsole ./src/main.py
Rename-Item -Path "./dist/main.exe" -NewName "SprayLoc_Pic_Optimizer.exe"

python ./create_zip_archive.py