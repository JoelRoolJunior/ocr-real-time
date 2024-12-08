from abc import ABC, abstractmethod


class ScreenCaptureBase(ABC):
    def __init__(self) -> None:
        self.isRunning = True
        self.img = None
        self.__x = 0
        self.__y = 0
        self.__width = 0
        self.__height = 0

    @property
    @abstractmethod
    def x(self):
        pass

    @x.setter
    @abstractmethod
    def x(self, x):
        pass

    @property
    @abstractmethod
    def y(self):
        pass

    @y.setter
    @abstractmethod
    def y(self, y):
        pass

    @property
    @abstractmethod
    def width(self):
        pass

    @width.setter
    @abstractmethod
    def width(self, width):
        pass

    @property
    @abstractmethod
    def height(self):
        pass

    @height.setter
    @abstractmethod
    def height(self, height):
        pass

    @property
    def rect(self):
        pass

    @abstractmethod
    def get_last_frame(self):
        pass

    @abstractmethod
    def loop_capture(self):
        pass
