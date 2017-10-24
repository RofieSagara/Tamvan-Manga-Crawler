# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject

from custom.widgetupdate import WidgetUpdate
from holder.search import Search
from holder.update import Update
from thread.downloadimagethread import DownloadImageThread
from thread.downloadmangathread import DownloadMangaThread
from thread.getlistbrowserlist import GetListBrowserList
from thread.getlistupdatethread import GetListUpdateThread
from view.infowindow import Ui_InfoWindow as Form


class Ui_MainWindow(QObject):
    signal = pyqtSignal(list)
    signal_image_download = pyqtSignal(int, int, Update)
    signal_download = pyqtSignal(int, int, int, int)
    signal_browser = pyqtSignal(list)
    signal_image_download_browser = pyqtSignal(int, int, Search)

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

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(200, 30, 639, 390))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.clicked.connect(self.tb_onclike)

        self.signal.connect(self.create_widget_update)
        self.signal_image_download.connect(self.refresh_widget_update)
        self.signal_browser.connect(self.create_widget_browser)
        self.get_browser_thread = GetListBrowserList(self.signal_browser)
        self.get_thread = GetListUpdateThread(self.signal)

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

        self.signal_download.connect(self.set_prog)
        self.thread_download = DownloadMangaThread(self.signal_download)
        self.thread_download.start()

        self.btnUpdate.clicked.connect(self.button_update_onclick)
        self.btnBrowse.clicked.connect(self.button_browser_onclick)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def set_prog(self, frm, total, max_image, now_image):
        self.prog.setMaximum(max_image)
        self.prog.setValue(now_image)
        self.prog.setFormat("Downloading Image ("+str(now_image)+"/"+str(max_image)+") %p%")
        if total == frm and max_image == now_image:
            self.status.setText("Waiting. . .")
            self.prog.setFormat("")
            self.prog.setMaximum(0)
            self.prog.setMinimum(0)
            self.prog.setValue(0)
        else:
            self.status.setText("Done "+str(frm)+", still "+str(total)+" Chapter left")

    def button_update_onclick(self):
        self.signal_image_download.connect(self.refresh_widget_update)
        self.queue_helper = DownloadImageThread(self.signal_image_download)
        self.get_thread.start()

    def button_browser_onclick(self):
        self.signal_image_download_browser.connect(self.refresh_image_browser)
        self.queue_helper = DownloadImageThread(self.signal_image_download_browser)
        self.get_browser_thread.start()

    def create_widget_browser(self, search_list):
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(30)
        self.tableWidget.clear()
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(631)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(220)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        idx = 0
        for n in search_list:
            wUpdate = WidgetUpdate()
            wUpdate.setGeometry(QtCore.QRect(210, 40, 631, 220))
            wUpdate.setAutoFillBackground(True)
            wUpdate.setObjectName("wUpdate")
            wUpdate.tag = n
            qpix = QtGui.QPixmap(os.path.join(os.getcwd(), "assets", "load_small.jpg"))
            scene = QtWidgets.QGraphicsScene()
            item = QtWidgets.QGraphicsPixmapItem(qpix)
            scene.addItem(item)
            imgCover = QtWidgets.QGraphicsView(scene, wUpdate)
            imgCover.setGeometry(QtCore.QRect(10, 10, 111, 131))
            imgCover.setObjectName("imgCover")
            lTitle = QtWidgets.QLabel(wUpdate)
            lTitle.setGeometry(QtCore.QRect(160, 10, 491, 21))
            lTitle.setObjectName("lTitle")
            lTitle.setText(n.title)
            lAlternative = QtWidgets.QLabel(wUpdate)
            lAlternative.setGeometry(QtCore.QRect(160, 40, 491, 41))
            lAlternative.setObjectName("lAlternative")
            lAutArtStRe = QtWidgets.QLabel(wUpdate)
            lAutArtStRe.setGeometry(QtCore.QRect(160, 90, 491, 21))
            lAutArtStRe.setObjectName("lAutArtStRe")
            lGenre = QtWidgets.QLabel(wUpdate)
            lGenre.setGeometry(QtCore.QRect(160, 120, 491, 17))
            lGenre.setObjectName("lGenre")
            lGenre.setText(n.genre[0]) #masih idex satu belum di for
            self.tableWidget.setCellWidget(idx, 0, wUpdate)
            self.queue_helper.add(idx, 0, n)
            idx += 1
        self.queue_helper.start()

    def refresh_image_browser(self, x, y, update_item):
        y = 0
        w_update = WidgetUpdate()
        w_update.setGeometry(QtCore.QRect(210, 40, 631, 220))
        w_update.setAutoFillBackground(True)
        w_update.setObjectName("wUpdate")
        w_update.tag = update_item
        p = w_update.palette()
        p.setColor(w_update.backgroundRole(), QtCore.Qt.red)
        w_update.setPalette(p)
        qpix = QtGui.QPixmap(update_item.small_cover_local)
        if not qpix.isNull():
            qpix = qpix.scaled(130, 190)
        else:
            qpix = QtGui.QPixmap(os.path.join(os.getcwd(), "assets", "error_small.jpg"))
            qpix = qpix.scaled(140, 200)
        scene = QtWidgets.QGraphicsScene()
        item = QtWidgets.QGraphicsPixmapItem(qpix)
        img_cover = QtWidgets.QGraphicsView(scene, w_update)
        img_cover.setGeometry(QtCore.QRect(10, 10, 140, 200))
        img_cover.setObjectName("imgCover")
        scene.addItem(item)
        l_title = QtWidgets.QLabel(w_update)
        l_title.setGeometry(QtCore.QRect(160, 10, 491, 21))
        l_title.setObjectName("lTitle")
        l_title.setText("<h4>"+update_item.title+"</h4>")
        l_alternative = QtWidgets.QLabel(w_update)
        l_alternative.setGeometry(QtCore.QRect(160, 40, 450, 90))
        l_alternative.setObjectName("lAlternative")
        l_alternative.setWordWrap(True)
        l_autartstre = QtWidgets.QLabel(w_update)
        l_autartstre.setGeometry(QtCore.QRect(160, 135, 450, 45))
        l_autartstre.setObjectName("lAutArtStRe")
        l_autartstre.setWordWrap(True)
        l_genre = QtWidgets.QLabel(w_update)
        l_genre.setGeometry(QtCore.QRect(160, 185, 450, 17))
        l_genre.setObjectName("lGenre")
        l_genre.setWordWrap(True)
        self.tableWidget.removeCellWidget(x, y)
        self.tableWidget.setCellWidget(x, y, w_update)
        img_cover.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tamvan Manga Downloader"))
        self.btnUpdate.setText(_translate("MainWindow", "Last Update"))
        self.btnBrowse.setText(_translate("MainWindow", "Browser"))

    def tb_onclike(self, clicked_index):
        data = self.tableWidget.cellWidget(clicked_index.row(), clicked_index.column()).tag
        print("Select :"+data.title)
        print("Position :row("+str(clicked_index.row())+") col(" + str(clicked_index.column())+")")
        dialog = QtWidgets.QDialog()
        link = data.link
        if "mangapark" in link:
            dialog.ui = Form(data.link)
        else:
            dialog.ui = Form("http://mangapark.me/"+data.link)
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def create_widget_update(self, update_list):
        idx = 0
        idy = 0
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(50)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(311)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(120)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        for n in update_list:
            w_update = WidgetUpdate()
            w_update.setGeometry(QtCore.QRect(0, 0, 311, 120))
            w_update.setAutoFillBackground(True)
            w_update.setObjectName("wUpdate")
            w_update.tag = n
            qpix = QtGui.QPixmap(os.path.join(os.getcwd(), "assets", "load_small.jpg"))
            scene = QtWidgets.QGraphicsScene()
            item = QtWidgets.QGraphicsPixmapItem(qpix)
            scene.addItem(item)
            img_cover = QtWidgets.QGraphicsView(scene, w_update)
            img_cover.setGeometry(QtCore.QRect(10, 10, 70, 100))
            img_cover.setObjectName("imgCover")
            l_title = QtWidgets.QLabel(w_update)
            l_title.setGeometry(QtCore.QRect(90, 10, 431, 17))
            l_title.setObjectName("lTitle")
            l_title.setText(n.title)
            t_chapter = ""
            for m in n.update_chapter:
                t_chapter = t_chapter + m.title + "\n"
            l_chapter = QtWidgets.QLabel(w_update)
            l_chapter.setGeometry(QtCore.QRect(90, 30, 431, 120))
            l_chapter.setObjectName("lChapter")
            l_chapter.setText(t_chapter)
            self.tableWidget.setCellWidget(idx, idy, w_update)
            self.queue_helper.add(idx, idy, n)
            if idy == 0:
                idy = 1
            else:
                idy = 0
                idx += 1
        self.queue_helper.start()

    def refresh_widget_update(self, x, y, update_item):
        w_update = WidgetUpdate()
        w_update.setGeometry(QtCore.QRect(0, 0, 311, 120))
        w_update.setAutoFillBackground(True)
        w_update.setObjectName("wUpdate")
        w_update.tag = update_item
        qpix = QtGui.QPixmap(update_item.small_cover_local)
        if not qpix.isNull():
            qpix = qpix.scaled(60, 93)
        else:
            qpix = QtGui.QPixmap(os.path.join(os.getcwd(), "assets", "error_small.jpg"))
            qpix = qpix.scaled(60, 93)
        scene = QtWidgets.QGraphicsScene()
        item = QtWidgets.QGraphicsPixmapItem(qpix)
        img_cover = QtWidgets.QGraphicsView(scene, w_update)
        img_cover.setGeometry(QtCore.QRect(10, 10, 70, 100))
        img_cover.setObjectName("imgCover")
        scene.addItem(item)
        l_title = QtWidgets.QLabel(w_update)
        l_title.setGeometry(QtCore.QRect(90, 10, 431, 17))
        l_title.setObjectName("lTitle")
        l_title.setText(update_item.title)
        t_chapter = ""
        for m in update_item.update_chapter:
            t_chapter = t_chapter + m.title + "\n"
        l_chapter = QtWidgets.QLabel(w_update)
        l_chapter.setGeometry(QtCore.QRect(90, 30, 431, 120))
        l_chapter.setObjectName("lChapter")
        l_chapter.setText(t_chapter)
        self.tableWidget.removeCellWidget(x, y)
        self.tableWidget.setCellWidget(x, y, w_update)
        img_cover.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
