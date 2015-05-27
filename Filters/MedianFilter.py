import cv2


class MedianFilter:
    _kSize = 1

    def __init__(self, kSize):
        self._kSize = kSize

    def do(self, img):
        return cv2.medianBlur(img, self._kSize)

    def getName(self):
        return 'MDN\(%d\)' % self._kSize