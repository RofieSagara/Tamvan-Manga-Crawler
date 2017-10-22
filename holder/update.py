from holder.manga import Manga


class Update(Manga):
    __small_cover = None
    __link = None
    __update_chapter = None
    __small_cover_local = None

    def __init__(self, title="", smallcover="", updatechapter=None, link=""):
        Manga.__init__(self, title)
        self.small_cover = smallcover
        self.update_chapter = updatechapter
        self.link = link

    @property
    def small_cover_local(self):
        return self.__small_cover_local

    @small_cover_local.setter
    def small_cover_local(self, value):
        self.__small_cover_local = value

    @property
    def small_cover(self):
        return self.__small_cover

    @small_cover.setter
    def small_cover(self, value):
        self.__small_cover = value

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, value):
        self.__link = value

    @property
    def update_chapter(self):
        return self.__update_chapter

    @update_chapter.setter
    def update_chapter(self, value):
        self.__update_chapter = value
