import cv2
import config
import numpy as np
from Logger import Logger


class AbstractImageProcessor:

    def __init__(self):
        pass

    def getImgFilename(self, prefix, number):
        return prefix + '/' + config.DEFAULT_IMGS_PATTERN.replace('%d', str(number))

    def openImg(self, filename):
        return cv2.imread(filename, cv2.CV_LOAD_IMAGE_UNCHANGED)

    def _imgsIsSimilar(self, image1, image2):
        return image1.shape == image2.shape and not (np.bitwise_xor(image1, image2).any())

    def process(self, imageNumbersForProcess, filters):
        numberLastCorrect = 1 #first image always skipped
        numberToSave = 1
        for imageNumber in imageNumbersForProcess:
            try:
                image = self.openImg(self.getImgFilename(config.DEFAULT_IMGS_DIR, imageNumber))
                prevImage = self.openImg(self.getImgFilename(config.DEFAULT_IMGS_DIR, numberLastCorrect))
                if self._imgsIsSimilar(image, prevImage):
                    raise Exception('Images is similar')

                outImg = self._processImage(image, prevImage)
                for filter in filters.values():
                    outImg = filter.do(outImg)
                cv2.imwrite(self.getImgFilename(config.DEFAULT_IMGS_OUT_DIR, numberToSave), outImg)

                Logger.write('processing image #%d OK' % imageNumber)
                numberLastCorrect = imageNumber
                numberToSave += 1
            except Exception as e:
                Logger.write('processing image #%d SKIPPED (%s)' % (imageNumber, e.message))

    def _processImage(self, image, prevImage):
        raise Exception('You must redeclare me!')