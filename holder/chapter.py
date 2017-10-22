
class Chapter:
    __link = None
    __title = None
    __time = None
    __image = None

    def __init__(self, link="", title="", time="", image=[]):
        self.link = link
        self.title = title
        self.time = time
        self.image = image

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        self.__image = value

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, value):
        self.__link = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        self.__time = value
