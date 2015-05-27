import cv2

#in construction
class NormalizationFilter:
    def __init__(self):
        pass

    def do(self, img):
        dstImage = img
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
        cv2.multiply(cv2.add(img, -minVal), 255 / (maxVal - minVal), dstImage)

        return dstImage

    def getName(self):
        return 'NRN'