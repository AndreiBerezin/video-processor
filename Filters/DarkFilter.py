import cv2

class DarkFilter:
    _darkImgFilename = ''

    def __init__(self, darkImgFilename):
        self._darkImgFilename = darkImgFilename

    def do(self, img):
        dstImage = img
        darkImage = cv2.imread(self._darkImgFilename, cv2.CV_LOAD_IMAGE_UNCHANGED)
        cv2.absdiff(darkImage, img, dstImage)

        return dstImage

    def getName(self):
        return 'DRK'