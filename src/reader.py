from typing import Text

import cv2


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
