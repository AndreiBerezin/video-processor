import sys

import config
from Logger import Logger
from FileSystem import FileSystem
from FiltersManager import FiltersManager

from VideoProcessors.DefaultVideoProcessor import DefaultVideoProcessor
from ImageProcessors.DiffPrevImageProcessor import DiffPrevImageProcessor


def action_explode(inputFilename):
    Logger.write('start explode video')
    videoProcessor = DefaultVideoProcessor()
    videoProcessor.splitVideo(inputFilename, config.DEFAULT_IMGS_DIR)
    return videoProcessor


def action_work():
    filterManager = FiltersManager()  # todo: add filters from config file
    # filterManager.addFilter(CropFilter(230, 263, 575, 530))
    #filterManager.addFilter(PseudoColorFilter())
    return filterManager


def action_implode(inputFilename, videoProcessor, filterManager):
    videoProcessor.work(DiffPrevImageProcessor(), filterManager.release())  # todo: get image processor from config file
    #videoProcessor.work(DiffMovingAverageDarkImageProcessor().init(30, 30, 'dark.png'), filterManager.release())

    Logger.write('start implode video')
    targetFilename = '%s_%s.avi' % (inputFilename, filterManager.getNames())
    videoProcessor.joinVideo(config.DEFAULT_IMGS_OUT_DIR, targetFilename)
    return targetFilename


def main(argv):
    if len(argv) != 2:
        print 'format: main.py <input>'
        return 1

    filesystem = FileSystem()
    filesystem.initDirs()

    videoProcessor = action_explode(argv[1])
    filterManager = action_work()
    targetFilename = action_implode(argv[1], videoProcessor, filterManager)

    Logger.write('end of work. created video in %s' % targetFilename)
    filesystem.deleteDirs()
    return 0


main(sys.argv)
