import cv2
from AbstractImageProcessor import AbstractImageProcessor
from Filters.MovingAverageFilter import MovingAverageFilter
from Filters.DarkFilter import DarkFilter


class DiffMovingAverageDarkImageProcessor(AbstractImageProcessor):
    _pixelsX = 0
    _pixelsY = 0
    _darkImgFilename = ''

    def init(self, pixelsX, pixelsY, darkImgFilename):
        self._pixelsX = pixelsX
        self._pixelsY = pixelsY
        self._darkImgFilename = darkImgFilename

        return self

    def _processImage(self, image, prevImage):
        if self._pixelsX == 0 or self._pixelsY == 0 or self._darkImgFilename == '':
            raise Exception('You must init image processor!')

        outImage = image

        dark = DarkFilter(self._darkImgFilename)
        outImage = dark.do(outImage)

        ma = MovingAverageFilter(self._pixelsX, self._pixelsY)
        outImage = ma.do(outImage)
        cv2.absdiff(outImage, image, outImage)

        return outImage
