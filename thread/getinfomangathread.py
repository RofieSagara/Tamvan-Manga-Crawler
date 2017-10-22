from PyQt5.QtCore import QThread, pyqtSignal
from core.mangapark import MangaPark
from holder.update import Update


class GetInfoMangaThread(QThread):

    def __init__(self, trigger, link):
        QThread.__init__(self)
        self.trigger = trigger
        self.link = link

    def run(self):
        up = Update(link=self.link)
        core = MangaPark()
        data = core.get_info(up)
        self.trigger.emit(data)
