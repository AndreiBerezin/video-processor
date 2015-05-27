import os
import sys, shutil
import config
from Logger import Logger


class FileSystem():
    def __init__(self):
        pass

    def deleteDirs(self):
        try:
            shutil.rmtree(config.DEFAULT_IMGS_DIR)
            shutil.rmtree(config.DEFAULT_IMGS_OUT_DIR)
        except Exception as e:
            pass  # nothing

    def _createDirs(self):
        os.makedirs(config.DEFAULT_IMGS_DIR)
        os.makedirs(config.DEFAULT_IMGS_OUT_DIR)

    def initDirs(self):
        Logger.write('making dir "%s"' % config.DEFAULT_IMGS_DIR)
        self.deleteDirs()
        self._createDirs()