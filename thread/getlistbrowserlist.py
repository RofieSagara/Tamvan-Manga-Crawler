from PyQt5.QtCore import QThread, pyqtSignal
from core.mangapark import MangaPark


class GetListBrowserList(QThread):
    __trigger = None

    def __init__(self, signal):
        QThread.__init__(self)
        self.__trigger = signal

    def run(self):
        core = MangaPark()
        data = core.get_search(1)
        print(len(data))
        self.__trigger.emit(data)
