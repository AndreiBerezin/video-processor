import cv2
import os
import numpy as np
import sys, shutil

from FiltersManager import FiltersManager
from Filters.MovingAverageFilter import MovingAverageFilter
from Filters.PseudoColorFilter import PseudoColorFilter

DEFAULT_IMGS_DIR = 'imgs'
DEFAULT_IMGS_OUT_DIR = 'imgs_out'
DEFAULT_IMGS_PATTERN = 'image%d.png'


def imgsIsSimilar(image1, image2):
    return image1.shape == image2.shape and not (np.bitwise_xor(image1, image2).any())

def getImgFilename(prefix, number):
    return prefix + '/' + DEFAULT_IMGS_PATTERN.replace('%d', str(number))

def openImg(filename):
    return cv2.imread(filename, cv2.CV_LOAD_IMAGE_UNCHANGED)


def processImage(imgNumber, lastCorrectImgNumber, numberToSave, filters):
    outImg = img = openImg(getImgFilename(DEFAULT_IMGS_DIR, imgNumber))

    if imgNumber == 1:
        return True

    prevImg = openImg(getImgFilename(DEFAULT_IMGS_DIR, lastCorrectImgNumber))
    if imgsIsSimilar(img, prevImg):
        return False

    for filter in filters.values():
        outImg = filter.do(outImg)

    #cv2.absdiff(prevImg, img, outImg)
    #outImg = outImg[200:530, 270:470]

    cv2.imwrite(getImgFilename(DEFAULT_IMGS_OUT_DIR, numberToSave), outImg)

    return True


def splitVideo(filename, targetDirName):
    command = 'ffmpeg -i %s %s/%s' % (filename, targetDirName, DEFAULT_IMGS_PATTERN)
    os.popen('%s' % command).read()

def joinVideo(dirname, targetFilename):
    command = 'ffmpeg -y -i %s/%s -vcodec rawvideo -pix_fmt bgr24 %s' % (dirname, DEFAULT_IMGS_PATTERN, targetFilename)
    os.popen('%s' % command).read()


def main(argv):
    if len(argv) != 2:
        print 'format: main.py <input>'

        return 1

    print 'making dir "%s"' % DEFAULT_IMGS_DIR
    try:
        shutil.rmtree(DEFAULT_IMGS_DIR)
        shutil.rmtree(DEFAULT_IMGS_OUT_DIR)
    except Exception as e:
        pass  # nothing
    os.makedirs(DEFAULT_IMGS_DIR)
    os.makedirs(DEFAULT_IMGS_OUT_DIR)

    print 'start explode video'
    splitVideo(argv[1], DEFAULT_IMGS_DIR)

    imgsCount = len([name for name in os.listdir(DEFAULT_IMGS_DIR)
                     if os.path.isfile(os.path.join(DEFAULT_IMGS_DIR, name))])
    print 'end explode video. images count=%d' % imgsCount

    filterManager = FiltersManager()
    filterManager.addFilter(MovingAverageFilter(2, 2))
    filterManager.addFilter(PseudoColorFilter())

    lastCorrect = 0
    numberToSave = 1
    for img in range(1, imgsCount + 1):
        status = processImage(img, lastCorrect, numberToSave, filterManager.release())
        if status == True:
            print 'processing image #%d OK' % img
            lastCorrect = img
            numberToSave += 1
        else:
            print 'processing image #%d SKIPPED' % img

    print 'start implode video'
    targetFilename = '%s_%s.avi' % (argv[1], filterManager.getNames())
    joinVideo(DEFAULT_IMGS_OUT_DIR, targetFilename)

    print 'end of work. created video in %s' % targetFilename
    shutil.rmtree(DEFAULT_IMGS_DIR)
    shutil.rmtree(DEFAULT_IMGS_OUT_DIR)

    return 0


main(sys.argv)
