from time import time

import numpy
from mss import mss

from ocr_real_time.CaptureBase import ScreenCaptureBase


class MssCapture(ScreenCaptureBase):
    def __init__(self) -> None:
        self.isRunning = True
        self.img = None
        self.__x = 0
        self.__y = 0
        self.__width = 100
        self.__height = 100

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.x = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def get_last_frame(self):
        return self.img

    @property
    def rect(self):
        """
        returns the dimensions of the capture area
        
        Examples:
            >>> capture = MssCapture()
            >>> capture.rect
            {'top': 0, 'left': 0, 'width': 100, 'height': 100}
        """
        return {
            'top': self.x,
            'left': self.y,
            'width': self.width,
            'height': self.height,
        }

    def loop_capture(self):
        with mss() as sct:
            while self.isRunning:
                self.img = numpy.array(sct.grab(self.rect))
