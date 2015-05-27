import cv2

import numpy as np
import sys, shutil
import config
from Logger import Logger
from FileSystem import FileSystem
from VideoProcessor import VideoProcessor

from FiltersManager import FiltersManager
from Filters.PseudoColorFilter import PseudoColorFilter
from Filters.CropFilter import CropFilter

from Processors.DiffPrevImageProcessor import DiffPrevImageProcessor


def main(argv):
    if len(argv) != 2:
        print 'format: main.py <input>'

        return 1

    filesystem = FileSystem()
    filesystem.initDirs()

    Logger.write('start explode video')
    videoProcessor = VideoProcessor()
    videoProcessor.splitVideo(argv[1], config.DEFAULT_IMGS_DIR)

    filterManager = FiltersManager()
    #filterManager.addFilter(CropFilter(230, 263, 575, 530))
    #filterManager.addFilter(PseudoColorFilter())
    videoProcessor.work(DiffPrevImageProcessor(), filterManager.release())

    Logger.write('start implode video')
    targetFilename = '%s_%s.avi' % (argv[1], filterManager.getNames())
    videoProcessor.joinVideo(config.DEFAULT_IMGS_OUT_DIR, targetFilename)

    Logger.write('end of work. created video in %s' % targetFilename)
    filesystem.deleteDirs()

    return 0

main(sys.argv)
