import cv2

class PseudoColorFilter:
    def __init__(self):
        pass

    def do(self, img):
        dstImage = img
        cv2.applyColorMap(img, cv2.COLORMAP_PINK, dstImage)

        return dstImage

    def getName(self):
        return 'PC'