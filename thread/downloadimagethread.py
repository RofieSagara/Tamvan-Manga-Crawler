from holder.queue import Queue
from PyQt5.QtCore import QThread, pyqtSignal
from tools.inputoutput import InputOutput


class DownloadImageThread(QThread):
    __list_queue = None

    def __init__(self, trigger):
        QThread.__init__(self)
        self.__list_queue = []
        self.trigger = trigger

    def add(self, x, y, update):
        data = Queue(x=x, y=y, update=update)
        self.__list_queue.append(data)

    @property
    def list_queue(self):
        return self.__list_queue

    def get_item_queue(self, x, y):
        for n in self.list_queue:
            if n.x == x and n.y == y:
                return n

    def run(self):
        lqueue = []
        for n in self.list_queue:
            url = n.update_item.small_cover
            core = InputOutput()
            loca_image = core.download_file(url)
            n.update_item.small_cover_local = loca_image
            data = Queue(x=n.x, y=n.y, update=n.update_item)
            lqueue.append(data)
            self.trigger.emit(n.x, n.y, n.update_item)
            self.sleep(0.1)
