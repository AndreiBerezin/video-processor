import cv2
import numpy as np

class MovingAverageFilter:
    _pixelsX = 0
    _pixelsY = 0

    def __init__(self, pixelsX, pixelsY):
        self._pixelsX = pixelsX
        self._pixelsY = pixelsY

    def do(self, img):
        kernel = np.ones((self._pixelsX, self._pixelsY), np.float32) / (self._pixelsX * self._pixelsY)

        return cv2.filter2D(img, -1, kernel)

    def getName(self):
        return 'MA\(%dx%d\)' % (self._pixelsX, self._pixelsY)