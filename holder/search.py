

class Search:

    __link = None
    __title = None
    __pic = None
    __rate = None
    __stat = None
    __relase = None
    __author = ""
    __genre = ""
    __altern = ""


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
    def pic(self):
        return self.__pic

    @pic.setter
    def pic(self, value):
        self.__pic = value

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
