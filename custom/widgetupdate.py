from PyQt5.QtWidgets import QWidget


class WidgetUpdate(QWidget):
    __tag = None

    def __init__(self):
        QWidget.__init__(self)

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, value):
        self.__tag = value
