from holder.queue import Queue
from PyQt5.QtCore import QThread, pyqtSignal
from tools.inputoutput import InputOutput
from core.mangapark import MangaPark
from holder.chapter import Chapter
from tools.enumhelper import FolderType
import os


class DownloadMangaThread(QThread):
    __number = 1
    __all_number = 0

    def __init__(self, trigger):
        QThread.__init__(self)
        self.trigger = trigger
        self.pause = True
        self.__number = 0
        self.__all_number = 0

    def run(self):
        while True:
            lfile = InputOutput.read_all_file()
            if len(lfile) > 0:
                self.__all_number = len(lfile)
                temp = open(lfile[0], "r").read().split("\n")
                url = temp[0]
                print(url)
                chapter = Chapter()
                chapter.link = url
                core = MangaPark()
                llink = core.get_image(chapter)
                title = temp[1]
                title_manga = temp[2]
                idx = 1
                for n in llink:
                    iot = InputOutput()
                    self.trigger.emit(self.__number, self.__all_number, len(llink), idx)
                    while True:
                        st = iot.download_file(n, FolderType.DOWNLOAD, title, title_manga)
                        if st is not None:
                            break
                    idx += 1
                InputOutput.delete_file(lfile[0])
                self.__number += 1
            else:
                self.pause = True
            if self.pause:
                self.trigger.emit(0, 0, 0, 0)
                print("Do Waiting")
                self.waiting()

    def waiting(self):
        while True:
            print("Waiting. . . .")
            lfile = InputOutput.read_all_file()
            if len(lfile) > 0:
                self.pause = False
                break
            self.sleep(5)
