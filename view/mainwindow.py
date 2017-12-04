# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from holder.search import Search
from holder.update import Update
from thread.downloadmangathread import DownloadMangaThread
from thread.getlistbrowserlist import GetListBrowserList
from thread.getlistupdatethread import GetListUpdateThread
from view import _mainwindow
from custom import qtablewidget


class Ui_MainWindow(QObject):
    signal_update = pyqtSignal(list)
    signal_image_download_update = pyqtSignal(int, int, Update)

    signal_browser = pyqtSignal(list)
    signal_image_download_browser = pyqtSignal(int, int, Search)

    signal_download = pyqtSignal(int, int, int, int)

    def __init__(self, parent=None):
        super().__init__(parent=None)
        self.thread_update = GetListUpdateThread(self.signal_update)
        self.thread_browser = GetListBrowserList(self.signal_browser)
        self.thread_download = DownloadMangaThread(self.signal_download)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(859, 450)
        MainWindow.setFixedSize(859, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lvGenre = QtWidgets.QListWidget(self.centralwidget)
        self.lvGenre.setGeometry(QtCore.QRect(10, 91, 181, 330))
        self.lvGenre.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.lvGenre.setObjectName("lvGenre")
        self.btnUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpdate.setGeometry(QtCore.QRect(10, 30, 181, 25))
        self.btnUpdate.setObjectName("btnUpdate")
        self.btnBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowse.setGeometry(QtCore.QRect(10, 60, 181, 25))
        self.btnBrowse.setObjectName("btnBrowse")

        # self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget = qtablewidget.QTableWidgetCustom(self.centralwidget, self)
        self.tableWidget.setGeometry(QtCore.QRect(200, 30, 639, 390))
        self.tableWidget.setObjectName("tableWidget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 859, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.prog = QtWidgets.QProgressBar(self.statusbar)
        self.prog.setGeometry(QtCore.QRect(10, 0, 600, 15))
        self.status = QtWidgets.QLabel(self.statusbar)
        self.status.setGeometry(QtCore.QRect(620, 0, 400, 15))
        self.status.setText("Standby")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.initialize_event()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tamvan Manga Downloader"))
        self.btnUpdate.setText(_translate("MainWindow", "Last Update"))
        self.btnBrowse.setText(_translate("MainWindow", "Browser"))

    def initialize_event(self):
        """
        Initialize Event, Thread , Signal
        :return:
        """
        self.signal_update.connect(self.create_widget_update)
        self.signal_image_download_update.connect(self.refresh_widget_update)
        self.signal_browser.connect(self.create_widget_browser)
        self.signal_download.connect(self.set_prog)

        self.thread_download.start()

        self.btnUpdate.clicked.connect(self.button_update_onclick)
        self.btnBrowse.clicked.connect(self.button_browser_onclick)
        self.tableWidget.clicked.connect(self.tb_onclike)

    def set_prog(self, frm, total, max_image, now_image):
        _mainwindow.set_prog(self, frm, total, max_image, now_image)

    def button_update_onclick(self):
        _mainwindow.button_update_onclick(self)

    def button_browser_onclick(self):
        _mainwindow.button_browser_onclick(self)

    def create_widget_browser(self, search_list):
        _mainwindow.create_widget_browser(self, search_list)

    def refresh_image_browser(self, x, y, update_item):
        _mainwindow.refresh_image_browser(self, x, y, update_item)

    def tb_onclike(self, clicked_index):
        _mainwindow.tb_onclike(self, clicked_index)

    def create_widget_update(self, update_list):
        _mainwindow.create_widget_update(self, update_list)

    def refresh_widget_update(self, x, y, update_item):
        _mainwindow.refresh_widget_update(self, x, y, update_item)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
