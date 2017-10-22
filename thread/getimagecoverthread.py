from PyQt5.QtCore import QThread, pyqtSignal
from tools.inputoutput import InputOutput


class GetImageCoverThread(QThread):

    def __init__(self, trigger, link=None):
        QThread.__init__(self)
        self.trigger = trigger
        self.link = link

    def set_link(self, link):
        self.link = link

    def run(self):
        core = InputOutput()
        data = core.download_file(self.link)
        self.trigger.emit(data)
