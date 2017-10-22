

class Queue:
    __update_item = None
    __x = None
    __y = None

    def __init__(self, update=None, x=None, y=None):
        self.update_item = update
        self.x = x
        self.y = y

    @property
    def update_item(self):
        return self.__update_item

    @update_item.setter
    def update_item(self, value):
        self.__update_item = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
