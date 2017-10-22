from holder.manga import Manga


class Info(Manga):
    __rating = None
    __rank = None
    __alternative = None
    __author = None
    __artist = None
    __genre = None
    __typemanga = None
    __release = None
    __status = None
    __cover = None
    __summary = None
    __chapter = None

    def __init__(self, title="", rating="",
                 rank="", alternative="",
                 author="", artist="",
                 genre="", typemanga="",
                 release="", status="",
                 cover="", summary="", chapter=None):
        Manga.__init__(self, title)
        self.rating = rating
        self.rank = rank
        self.alternative = alternative
        self.author = author
        self.artist = artist
        self.genre = genre
        self.release = release
        self.typemanga = typemanga
        self.status = status
        self.cover = cover
        self.summary = summary
        self.chapter = chapter

    @property
    def chapter(self):
        return self.__chapter

    @chapter.setter
    def chapter(self, value):
        self.__chapter = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, value):
        self.__rank = value

    @property
    def alternative(self):
        return self.__alternative

    @alternative.setter
    def alternative(self, value):
        self.__alternative = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    @property
    def artist(self):
        return self.__artist

    @artist.setter
    def artist(self, value):
        self.__artist = value

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        self.__genre = value

    @property
    def release(self):
        return self.__release

    @release.setter
    def release(self, value):
        self.__release = value

    @property
    def typemanga(self):
        return self.__typemanga

    @typemanga.setter
    def typemanga(self, value):
        self.__typemanga = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def cover(self):
        return self.__cover

    @cover.setter
    def cover(self, value):
        self.__cover = value

    @property
    def summary(self):
        return self.__summary

    @summary.setter
    def summary(self, value):
        self.__summary = value
