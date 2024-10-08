import time
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QPushButton,
                             QToolBar,
                             QLabel,
                             QWidget,
                             QVBoxLayout,
                             QAction,
                             QLineEdit,
                             QSpacerItem,
                             QSizePolicy,
                             QMessageBox,
                             QProgressBar)
from PyQt5.QtCore import Qt
from .controllers import descargar_video
from settings import ICON_DIR

class MainView:
    def __init__(self, mainapp):
        self.toolbar = QToolBar('NavBar', mainapp)
        #Etiquetas
        self.label = QLabel('Tiene la Opcionde De Descargar Auidos y Videos', mainapp)
        self.title_yt = QLabel('', mainapp)
        #Botones
        self.button = QPushButton('Descargar', mainapp)
        self.logo_button = QAction(QIcon(ICON_DIR.resolve().as_posix()), 'YT_Download', mainapp)
        #Inputs
        self.url_video_yt = QLineEdit(mainapp)
        #ProgresBar
        self.progres_bar = QProgressBar()
        self.container = QWidget()
        self.layout = QVBoxLayout(self.container)
        self.mainapp = mainapp


    def setup_ui(self) -> None:
        try:
            self.set_toolbar()

            self.set_labels()

            self.set_buttons()

            self.set_progres_bar()

            self.load_layout()

            self.mainapp.setCentralWidget(self.container)

        except Exception as e:
            print('Error: {}\nData: {}'.format(e.__class__, e.args))

    #Generadores de UI
    def set_buttons(self):
        self.button.clicked.connect(self.on_click)

    def set_labels(self):
        self.label.setFixedHeight(30)

    def set_inputs(self):
        self.url_video_yt.setPlaceholderText('Ingrese la URL del Video: ')

    def set_progres_bar(self):
        self.progres_bar.setValue(0)
        self.progres_bar.setVisible(False)

    def load_layout(self):
        self.layout.addWidget(self.label, alignment=Qt.AlignTop | Qt.AlignHCenter)
        self.layout.addWidget(self.url_video_yt, alignment=Qt.AlignHCenter)
        self.layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.layout.addWidget(self.title_yt, alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.progres_bar, alignment=Qt.AlignBottom)
        self.layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.layout.addWidget(self.button, alignment=Qt.AlignHCenter)

    def set_toolbar(self):
        self.toolbar.setMovable(False)
        self.toolbar.setFloatable(False)
        self.toolbar.setOrientation(Qt.Horizontal)
        self.logo_button.setToolTip('Logo')
        self.toolbar.addAction(self.logo_button)
        self.mainapp.addToolBar(self.toolbar)


    def message(self, msg:str, info:str, a0:bool = False) -> bool:
        try:
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Warning)
            alert.setText(msg)
            alert.setInformativeText(info)
            alert.setWindowTitle('Mensaje')
            alert.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) if not a0 else alert.setStandardButtons(QMessageBox.Close | QMessageBox.Cancel)

            response = alert.exec_()

            return response == QMessageBox.Ok if not a0 else (response == QMessageBox.Close)

        except Exception as e:
            print('Error: {}\nData: {}'.format(e.__class__, e.args))

    #Funciones Handler
    def on_click(self) -> None:
        try:
            url = self.url_video_yt.text()
            if url:
                self.progres_bar.setVisible(True)
                ok = descargar_video(url, self.load_bar, self.finish_load)
                if ok:
                    pass
                else:
                    self.progres_bar.setVisible(False)
                    self.message('Error', 'No se pudeo descargar el video')
            else:
                self.message('Error', 'Si no se presenta URL no se puede buscar')

        except Exception as e:
            print('Error: {}\nData: {}'.format(e.__class__, e.args))
            self.message('Opss', 'Se detecto un Error: {}'.format(e.args))

    def load_bar(self, stream, chunk, bytes_remaining):
        try:
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            porcent = int(bytes_downloaded/total_size*100)

            self.title_yt.setText('Titulo: {}, Completado en un: {}'.format(stream.title, porcent))
            self.progres_bar.setValue(porcent)
        except Exception as e:
            print('Error: {}\nData: {}'.format(e.__class__, e.args))
            self.message('Opss', 'Se detecto un Error: {}'.format(e.args))

    def finish_load(self, stream, path:str):
        try:
            time.sleep(4.0)
            self. progres_bar.setVisible(False)
            self.progres_bar.setValue(0)
            self.title_yt.setText('Terminado')
            self.url_video_yt.setText('')
            self.message('Ruta del archivo', 'El Archivo Fue Guardado En: {}\nCon El Nombre: {}'.format(path, stream.title))
        except Exception as e:
            print('Error: {}\nData: {}'.format(e.__class__, e.args))
            self.message('Opss', 'Se detecto un Error: {}'.format(e.args))
