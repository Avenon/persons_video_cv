from typing import Text

import cv2
import streamlink


class VideoFileReader(object):
    """
    Объект чтения видео файла с диска, для выполнения различных действий
    над ним
    """

    def __init__(self, file_path: Text):
        self.capture = cv2.VideoCapture(str(file_path))
        self.frame_count = int(self.capture.get(cv2.CAP_PROP_FRAME_COUNT))
        # Массив кадров, который преобразуется в тензор
        self.__image_list = []
        while self.capture.isOpened():
            ret, frame = self.capture.read()
            if ret:
                self.__image_list.append(frame)
            else:
                break
        self.capture.release()

    @property
    def get_frames(self) -> list:
        return self.__image_list


class YouTubeReader(object):
    """
    Объект чтения видео с ютуба в реальном времени
    """

    def __init__(self, url: Text):
        streams = streamlink.streams(url)
        self.capture = cv2.VideoCapture(streams["best"].url)

    def show_video(self):
        while True:
            ret, frame = self.capture.read()
            print(frame)
            cv2.imshow("frame", frame)

            # Для выхода нужно нажать q
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
