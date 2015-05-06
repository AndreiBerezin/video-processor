import cv2
import numpy as np

class PseudoColorFilter:
    def __init__(self):
        pass

    def do(self, img):
        #меняет на какое то аццкое почти белое изображение :(
        lookupTable = np.arange(255, -1, -1, dtype = img.dtype)
        lut3 = np.column_stack((lookupTable, lookupTable, lookupTable))
        lutIdxDot = np.array( [0, 1, 2], dtype=int)
        lutIdx0 = np.zeros( img.shape[0] * img.shape[1], dtype=int)
        lutIdx1 = np.ones( img.shape[0] * img.shape[1], dtype=int)
        lutIdx2 = lutIdx1 * 2
        lutIdx = np.column_stack((lutIdx0, lutIdx1, lutIdx2))
        lutIdx.shape = img.shape

        return lut3[img, lutIdx]

        #правильнее через LUT, но непонятно как заполнять lookupTable
        #dstImage = img
        #cv2.LUT(img, lookupTable, dstImage)
        #return dstImage

    def getName(self):
        return 'PC'