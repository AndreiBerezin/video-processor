import cv2
import os
import numpy as np
import sys, shutil

DEFAULT_IMGS_DIR = 'imgs'
DEFAULT_IMGS_OUT_DIR = 'imgs_out'
DEFAULT_IMGS_PATTERN = 'image%d.png'

def isSimilar(image1, image2):
    return image1.shape == image2.shape and not(np.bitwise_xor(image1, image2).any())

def processImage(imgNumber, lastCorrectImgNumber, numberToSave):
    filename = DEFAULT_IMGS_DIR + '/' + DEFAULT_IMGS_PATTERN.replace('%d', str(imgNumber))
    img = cv2.imread(filename, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    outImg = img

    if imgNumber > 1:
        filenamePrev = DEFAULT_IMGS_DIR + '/' + DEFAULT_IMGS_PATTERN.replace('%d', str(lastCorrectImgNumber))
        prevImg = cv2.imread(filenamePrev, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        if isSimilar(img, prevImg):
            return False
        cv2.absdiff(img, prevImg, outImg)

    outFilename = DEFAULT_IMGS_OUT_DIR + '/' + DEFAULT_IMGS_PATTERN.replace('%d', str(numberToSave))
    cv2.imwrite(outFilename, outImg)
    return True

def splitVideo(filename, targetDirName):
    command = 'ffmpeg -i %s %s/%s' % (filename, targetDirName, DEFAULT_IMGS_PATTERN)
    os.popen('%s' % command).read()


def joinVideo(dirname, targetFilename):
    #command = 'ffmpeg -f image2 -y -i %s/%s -vcodec png %s' % (dirname, DEFAULT_IMGS_PATTERN, targetFilename)
    command = 'ffmpeg -y -i %s/%s -vcodec rawvideo -pix_fmt bgr24 %s' % (dirname, DEFAULT_IMGS_PATTERN, targetFilename)
    os.popen('%s' % command).read()


def main(argv):
    if len(argv) != 3:
        print 'format: main.py <input> <output>'

        return 1

    print 'making dir "%s"' % DEFAULT_IMGS_DIR
    try:
        shutil.rmtree(DEFAULT_IMGS_DIR)
        shutil.rmtree(DEFAULT_IMGS_OUT_DIR)
    except Exception as e:
        pass # nothing
    os.makedirs(DEFAULT_IMGS_DIR)
    os.makedirs(DEFAULT_IMGS_OUT_DIR)

    print 'start explode video'
    splitVideo(argv[1], DEFAULT_IMGS_DIR)

    imgsCount = len([name for name in os.listdir(DEFAULT_IMGS_DIR) if os.path.isfile(os.path.join(DEFAULT_IMGS_DIR, name))])
    print 'end explode video. images count=%d' % imgsCount

    lastCorrect = 0
    numberToSave = 1
    for img in range(1, imgsCount + 1):
        print 'processing image #%d' % img
        status = processImage(img, lastCorrect, numberToSave)
        if status == True:
            lastCorrect = img
            numberToSave += 1

    print 'start implode video'
    joinVideo(DEFAULT_IMGS_OUT_DIR, argv[2])

    print 'end of work'
    shutil.rmtree(DEFAULT_IMGS_DIR)
    shutil.rmtree(DEFAULT_IMGS_OUT_DIR)

    return 0


main(sys.argv)
