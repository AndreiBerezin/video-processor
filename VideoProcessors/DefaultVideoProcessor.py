import os
import config
from Logger import Logger


class DefaultVideoProcessor:
    def __init__(self):
        pass

    def splitVideo(self, filename, targetDirName):
        command = 'ffmpeg -i %s %s/%s' % (filename, targetDirName, config.DEFAULT_IMGS_PATTERN)
        os.popen('%s' % command).read()

    def joinVideo(self, dirname, targetFilename):
        command = 'ffmpeg -y -i %s/%s %s %s' % (
            dirname, config.DEFAULT_IMGS_PATTERN, config.JOIN_VIDEO_PARAMS, targetFilename)
        os.popen('%s' % command).read()

    def _getImageNumbersForProcess(self):
        imagesCount = len([name for name in os.listdir(config.DEFAULT_IMGS_DIR)
                        if os.path.isfile(os.path.join(config.DEFAULT_IMGS_DIR, name))])

        return range(1, imagesCount + 1)

    def work(self, imageProcessor, filters):
        if not imageProcessor:
            raise Exception('No image processor for work')

        imageNumbersForProcess = self._getImageNumbersForProcess()
        Logger.write('end explode video. images count=%d' % len(imageNumbersForProcess))
        imageProcessor.process(imageNumbersForProcess, filters)