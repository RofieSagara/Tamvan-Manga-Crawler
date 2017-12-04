from PyQt5.QtCore import QThread, pyqtSignal
from core.mangapark import MangaPark


class GetListBrowserList(QThread):
    __trigger = None

    def __init__(self, signal, ide=1):
        QThread.__init__(self)
        self.__trigger = signal
        self.ide = ide

    def set_id(self, ide):
        self.ide = ide

    def get_next(self):
        self.ide += 1

    def run(self):
        core = MangaPark()
        data = core.get_search(self.ide)
        print(len(data))
        self.__trigger.emit(data)
