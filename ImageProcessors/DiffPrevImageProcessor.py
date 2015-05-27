import cv2
from AbstractImageProcessor import AbstractImageProcessor


class DiffPrevImageProcessor(AbstractImageProcessor):

    def _processImage(self, image, prevImage):
        outImage = image
        cv2.absdiff(prevImage, image, outImage)

        return outImage
