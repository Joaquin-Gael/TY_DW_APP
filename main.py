import sys
import time
from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from app.core import MainApp, aplly_styles, Path

def main():
    try:
        app = QApplication(sys.argv)

        splash_pix = QPixmap(Path(__file__).parent.as_posix() + '/app/resources/img/YT_Download.png')
        splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
        splash.setWindowFlag(Qt.FramelessWindowHint)
        splash.show()

        app.processEvents()

        for i in range(10):
            splash.showMessage("Cargando la aplicación, por favor espera... {}".format(i*10), Qt.AlignBottom | Qt.AlignCenter, Qt.white)
            time.sleep(0.2)

        aplly_styles(app)

        window = MainApp()

        splash.finish(window)

        window.show()

        sys.exit(app.exec_())
    except Exception as e:
        print('Error: {}\nData: {}'.format(e.__class__, e.args))


if __name__ == '__main__':
    main()