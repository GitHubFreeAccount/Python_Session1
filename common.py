from __future__ import print_function
import os
import shutil


class Options(object):
    def __init__(self):
        base_out_path = os.getenv('OUT_DIR_COMMON_BASE')
        if base_out_path is None:
            base_out_path = 'out'
        else:
            base_search_path = os.path.join(base_out_path, os.path.basename(os.getcwd()))

        self.tempfiles = []


OPTIONS = Options()


def Cleanup():
    for i in OPTIONS.tempfiles:
        if os.path.isdir(i):
            shutil.rmtree(i, ignore_errors=True)
        else:
            os.remove(i)
    del OPTIONS.tempfiles[:]
