from PyQt5.QtCore import QThread, pyqtSignal
from core.mangapark import MangaPark


class GetListUpdateThread(QThread):

    def __init__(self, signal):
        QThread.__init__(self)
        self.trigger = signal

    def run(self):
        core = MangaPark()
        result = core.get_update()
        print(len(result))
        self.trigger.emit(result)
