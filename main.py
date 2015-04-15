import cv2
import os
import sys, shutil

DEFAULT_IMGS_DIR = 'imgs'
DEFAULT_IMGS_PATTERN = 'image%d.png'

def processImage(filename):
    img = cv2.imread(filename, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    (thresh, im_bw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imwrite(filename, im_bw)


def explodeVideo(filename, targetDirName):
    command = 'ffmpeg -i %s %s/%s' % (filename, targetDirName, DEFAULT_IMGS_PATTERN)
    os.popen('%s' % command).read()


def implodeVideo(dirname, targetFilename):
    command = 'ffmpeg -f image2 -y -i %s/%s -vcodec png %s' % (dirname, DEFAULT_IMGS_PATTERN, targetFilename)
    os.popen('%s' % command).read()


def main(argv):
    try:
        if len(argv) != 3:
            raise Exception('format: main.py <input> <output>')
    except Exception as e:
        print e.message
        return 1

    print 'making dir "%s"' % DEFAULT_IMGS_DIR
    try:
        shutil.rmtree(DEFAULT_IMGS_DIR)
    except Exception as e:
        pass # nothing
    os.makedirs(DEFAULT_IMGS_DIR)

    print 'start explode video'
    explodeVideo(argv[1], DEFAULT_IMGS_DIR)

    imgsCount = len([name for name in os.listdir(DEFAULT_IMGS_DIR) if os.path.isfile(os.path.join(DEFAULT_IMGS_DIR, name))])
    print 'end explode video. images count=%d' % imgsCount

    for img in range(1, imgsCount + 1):
        print 'processing image #%d' % img
        processImage(DEFAULT_IMGS_DIR + '/' + DEFAULT_IMGS_PATTERN.replace('%d', str(img)))

    print 'start implode video'
    implodeVideo(DEFAULT_IMGS_DIR, argv[2])

    print 'end of work'
    shutil.rmtree(DEFAULT_IMGS_DIR)

    return 0


main(sys.argv)

#ffmpeg -i video.avi -vcodec libx264 -pix_fmt yuv420p -b:v 200000k output.mp4