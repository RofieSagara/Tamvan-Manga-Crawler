from PyQt5 import QtCore, QtWidgets
from view import _mainwindow


class QScene(QtWidgets.QGraphicsScene):

    def __init__(self, obj, idx, idy, *args, **kwds):
        QtWidgets.QGraphicsScene.__init__(self, *args, **kwds)
        self.obj = obj
        self.idx = idx
        self.idy = idy

    def mousePressEvent(self, ev):
        if ev.button() == QtCore.Qt.LeftButton:
            data = QtCore.QModelIndex()
            _mainwindow.tb_onclike(self.obj, data, self.idx, self.idy)
