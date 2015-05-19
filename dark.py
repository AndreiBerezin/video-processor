import cv2
import os
import numpy as np
import sys, shutil

DEFAULT_IMGS_DIR = 'imgs'
DEFAULT_IMGS_OUT_DIR = 'imgs_out'
DEFAULT_IMGS_PATTERN = 'image%d.png'


def getImgFilename(prefix, number):
    return prefix + '/' + DEFAULT_IMGS_PATTERN.replace('%d', str(number))

def openImg(filename):
    return cv2.imread(filename, cv2.CV_LOAD_IMAGE_UNCHANGED)

def splitVideo(filename, targetDirName):
    command = 'ffmpeg -i %s %s/%s' % (filename, targetDirName, DEFAULT_IMGS_PATTERN)
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

    print 'end explode video'

    for img in range(1, 11):
        out = openImg(getImgFilename(DEFAULT_IMGS_DIR, img))
        cv2.imwrite(getImgFilename(DEFAULT_IMGS_OUT_DIR, img), out)

    for img in range(2, 11):
        curImg = openImg(getImgFilename(DEFAULT_IMGS_DIR, img))
        firstImg = openImg(getImgFilename(DEFAULT_IMGS_DIR, 1))
        outImg = np.add(firstImg, curImg)
        cv2.imwrite(getImgFilename(DEFAULT_IMGS_OUT_DIR, 1), outImg)

    firstImg = openImg(getImgFilename(DEFAULT_IMGS_DIR, 1))
    outImg = np.multiply(firstImg, 0.1)
    cv2.imwrite(getImgFilename(DEFAULT_IMGS_OUT_DIR, 55), outImg)

    return 0

main(sys.argv)
