pyinstaller --icon=./favicon.ico --onefile --noconsole ./src/main.py
Rename-Item -Path "./dist/main.exe" -NewName "SprayLoc_Pic_Converter.exe"