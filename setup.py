from PyInstaller.__main__ import run

options = [
    '--onefile',
    '--windowed',
    '--name=YT_Download',
    '--add-data=app/resources/img;app/resources/img',
    '--add-data=app/resources/styles.qss;app/resources',
    '--icon=app/resources/img/YT_DW.ico',
    'main.py'
]
run(options)