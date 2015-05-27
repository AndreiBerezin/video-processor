import cv2


class GaussianFilter:
    _pixelsX = 0
    _pixelsY = 0

    def __init__(self, pixelsX, pixelsY):
        self._pixelsX = pixelsX
        self._pixelsY = pixelsY

    def do(self, img):
        return cv2.GaussianBlur(img, (self._pixelsX, self._pixelsY), 0)

    def getName(self):
        return 'GSN\(%dx%d\)' % (self._pixelsX, self._pixelsY)