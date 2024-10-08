from pathlib import Path

from six import reraise


def get_descktop():
    path = Path.home() / 'Desktop'
    path_es = Path.home() / 'Escritorio'

    if path.exists() and path.is_dir():
        return path
    elif path_es.exists() and path.is_dir():
        return path_es
    else:
        path = Path.home() / 'OneDrive' / 'Desktop'
        path_es = Path.home() / 'OneDrive' / 'Escritorio'
        if path.exists() and path.is_dir():
            return path
        elif path_es.exists() and path_es.is_dir():
            return path_es
        else:
            raise FileNotFoundError(f'No se encontró el directorio: {path}')


STYLES_PATH = Path(__file__).parent / 'app' / 'resources' / 'styles.qss'
ICON_DIR = Path(__file__).parent / 'app' / 'resources' / 'img' / 'YT_DW.ico'

OUTPUT_PATH = get_descktop()

WINDOW_H:int = 700
WINDOW_W:int = 800

WINDOW_Y:float = 4.5
WINDOW_X:float = 3.5