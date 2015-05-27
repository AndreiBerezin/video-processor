import sys

import config
from Logger import Logger
from FileSystem import FileSystem

from VideoProcessors.DarkGenerationVideoProcessor import DarkGenerationVideoProcessor
from ImageProcessors.AbstractImageProcessor import AbstractImageProcessor


def main(argv):
    if len(argv) != 2:
        print 'format: dark.py <input>'

        return 1

    filesystem = FileSystem()
    filesystem.initDirs()

    Logger.write('start explode video')
    videoProcessor = DarkGenerationVideoProcessor()
    videoProcessor.splitVideo(argv[1], config.DEFAULT_IMGS_DIR)

    videoProcessor.work(AbstractImageProcessor(), [])

    Logger.write('end of work. created dark.png')
    filesystem.deleteDirs()

    return 0

main(sys.argv)
