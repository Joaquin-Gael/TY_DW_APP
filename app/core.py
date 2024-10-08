import ctypes
import sys
import os
from pathlib import Path
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from .views import MainView
from settings import WINDOW_W, WINDOW_H, WINDOW_X, WINDOW_Y, STYLES_PATH, ICON_DIR


def get_resource_path(relative_path: str) -> str:
    """Retorna la ruta correcta al recurso, ya sea en el ejecutable empaquetado o en desarrollo."""
    try:
        # Si está empaquetado, sys._MEIPASS apunta al directorio temporal
        base_path = sys._MEIPASS
    except AttributeError:
        # Si no está empaquetado, usa la ruta normal del archivo
        base_path = Path(__file__).parent

    return os.path.join(base_path, relative_path)


# Ajustar las rutas de los recursos usando get_resource_path
STYLES_PATH = get_resource_path('app/resources/styles.qss')
ICON_DIR = get_resource_path('app/resources/img/YT_DW.ico')


def aplly_styles(app: QApplication):
    try:
        with open(STYLES_PATH, 'r') as file:
            app.setStyleSheet(file.read())
    except Exception as e:
        print('Error: {}\nData: {}'.format(e.__class__, e.args))

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MainView(self)
        self.user32 = ctypes.windll.user32
        self._x = int(self.user32.GetSystemMetrics(0) / WINDOW_X)
        self._y = int(self.user32.GetSystemMetrics(1) / WINDOW_Y)

        # Configuración de la ventana
        self.setWindowTitle("YT_Download")
        self.setGeometry(self._x, self._y, WINDOW_W, WINDOW_H)
        self.setWindowIcon(QIcon(ICON_DIR))

        self.ui.setup_ui()

    def closeEvent(self, a0):
        try:
            response = self.ui.message('Cerrar?','Seguro de quere cerrar el progaram?', True)
            if response:
                a0.accept()
            else:
                a0.ignore()

        except Exception as e:
            print('Error: {}\nData: {}'.format(e.__class__, e.args))