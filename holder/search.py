from holder.manga import Manga


class Search(Manga):
    __link = None
    __small_cover = None
    __small_cover_local = None
    __rate = None
    __stat = None
    __relase = None
    __author = ""
    __genre = ""
    __altern = ""

    def __init__(self, title=None):
        Manga.__init__(self, title)

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, value):
        self.__link = value

    @property
    def small_cover(self):
        return self.__small_cover

    @small_cover.setter
    def small_cover(self, value):
        self.__small_cover = value

    @property
    def small_cover_local(self):
        return self.__small_cover_local

    @small_cover_local.setter
    def small_cover_local(self, value):
        self.__small_cover_local = value

    @property
    def stat(self):
        return self.__stat

    @stat.setter
    def stat(self, value):
        self.__stat = value

    @property
    def relase(self):
        return self.__relase

    @relase.setter
    def relase(self, value):
        self.__relase = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        self.__genre = value

    @property
    def altern(self):
        return self.__altern

    @altern.setter
    def altern(self, value):
        self.__altern = value

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, value):
        self.__rate = value
