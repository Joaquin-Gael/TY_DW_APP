from pytubefix import YouTube
from pytubefix.exceptions import PytubeFixError
from settings import OUTPUT_PATH
from typing import Any


def descargar_video(url:str, load:Any = lambda e, a, b: None, finish: Any = lambda e, a: None) -> bool:
    try:
        yt = YouTube(url, on_progress_callback=load, on_complete_callback=finish)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=OUTPUT_PATH)
        return True
    except Exception as e:
        print('Error: {}\nData: {}'.format(e.__class__, e.args))
        return False

    except PytubeFixError as e:
        print('Error: {}\nData: {}'.format(e.__class__, e.args))
        return False