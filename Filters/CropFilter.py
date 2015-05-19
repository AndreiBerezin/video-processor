class CropFilter:
    _fromX = 0
    _fromY = 0
    _toX = 0
    _toY = 0

    def __init__(self, fromX, fromY, toX, toY):
        self._fromX = fromX
        self._fromY = fromY
        self._toX = toX
        self._toY = toY

    def do(self, img):
        return img[self._fromY:self._toY, self._fromX:self._toX]

    def getName(self):
        return 'CRP'