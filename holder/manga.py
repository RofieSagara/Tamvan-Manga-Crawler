
class Manga:
    __title = None

    def __init__(self, title=""):
        self.title = title

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value
