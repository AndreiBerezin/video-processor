import cv2
import numpy as np
import config
import shutil
from DefaultVideoProcessor import DefaultVideoProcessor

class DarkGenerationVideoProcessor(DefaultVideoProcessor):

    def work(self, imageProcessor, filters):
        if not imageProcessor:
            raise Exception('No image processor for work')

        for imageNumber in range(1, 11):
            outImage = imageProcessor.openImg(imageProcessor.getImgFilename(config.DEFAULT_IMGS_DIR, imageNumber))
            cv2.imwrite(imageProcessor.getImgFilename(config.DEFAULT_IMGS_OUT_DIR, imageNumber), outImage)

        for imageNumber in range(2, 11):
            currentImage = imageProcessor.openImg(imageProcessor.getImgFilename(config.DEFAULT_IMGS_DIR, imageNumber))
            firstImage = imageProcessor.openImg(imageProcessor.getImgFilename(config.DEFAULT_IMGS_DIR, 1))
            outImage = np.add(firstImage, currentImage)
            cv2.imwrite(imageProcessor.getImgFilename(config.DEFAULT_IMGS_OUT_DIR, 1), outImage)

        firstImg = imageProcessor.openImg(imageProcessor.getImgFilename(config.DEFAULT_IMGS_DIR, 1))
        outImg = np.multiply(firstImg, 0.1)

        finalFileName = imageProcessor.getImgFilename(config.DEFAULT_IMGS_OUT_DIR, 55)
        cv2.imwrite(finalFileName, outImg)

        shutil.copy(finalFileName, 'dark.png')