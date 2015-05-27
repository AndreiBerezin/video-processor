import cv2
from AbstractImageProcessor import AbstractImageProcessor


class DiffPrevImageProcessor(AbstractImageProcessor):

    def _processImage(self, image, prevImage):
        outImage = image
        cv2.absdiff(prevImage, image, outImage)

        '''
        dark = DarkFilter('dark.png')
        outImg = dark.do(outImg)
        ma = MovingAverageFilter(2, 2)
        outImg = ma.do(outImg)
        cv2.absdiff(outImg, img, outImg)
        '''

        return outImage
