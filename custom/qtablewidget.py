from PyQt5 import QtWidgets
from view import _mainwindow


class QTableWidgetCustom(QtWidgets.QTableWidget):
    lidx = 0
    lidy = 0
    last_get = 0

    def __init__(self, layout, obj):
        QtWidgets.QTableWidget.__init__(self, layout)
        self.obj = obj

    def verticalScrollbarValueChanged(self, p_int):
        super().verticalScrollbarValueChanged(p_int)
        print("v change: ", p_int, " from", self.rowCount()-1)
        if p_int == self.rowCount()-1 and self.rowCount()-1 != self.last_get:
            _mainwindow.get_browser_more(self.obj)
            self.last_get = self.rowCount()-1

    def set_last_idx_idy(self, idx, idy):
        self.lidx = idx
        self.lidy = idy
