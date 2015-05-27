import sys

import config
from Logger import Logger
from FileSystem import FileSystem
from FiltersManager import FiltersManager

from VideoProcessors.DefaultVideoProcessor import DefaultVideoProcessor
from ImageProcessors.DiffPrevImageProcessor import DiffPrevImageProcessor


def main(argv):
    if len(argv) != 2:
        print 'format: main.py <input>'

        return 1

    filesystem = FileSystem()
    filesystem.initDirs()

    Logger.write('start explode video')
    videoProcessor = DefaultVideoProcessor()
    videoProcessor.splitVideo(argv[1], config.DEFAULT_IMGS_DIR)

    filterManager = FiltersManager()
    # filterManager.addFilter(CropFilter(230, 263, 575, 530))
    #filterManager.addFilter(PseudoColorFilter())

    videoProcessor.work(DiffPrevImageProcessor(), filterManager.release())
    #videoProcessor.work(DiffMovingAverageDarkImageProcessor().init(30, 30, 'dark.png'), filterManager.release())

    Logger.write('start implode video')
    targetFilename = '%s_%s.avi' % (argv[1], filterManager.getNames())
    videoProcessor.joinVideo(config.DEFAULT_IMGS_OUT_DIR, targetFilename)

    Logger.write('end of work. created video in %s' % targetFilename)
    filesystem.deleteDirs()

    return 0


main(sys.argv)
