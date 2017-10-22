# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from thread.getlistupdatethread import GetListUpdateThread
from custom.widgetupdate import WidgetUpdate
from thread.downloadimagethread import DownloadImageThread
from holder.update import Update
from infowindow import Ui_InfoWindow as Form
from thread.downloadmangathread import DownloadMangaThread


class Ui_MainWindow(QObject):
    signal = pyqtSignal(list)
    signal_image_download = pyqtSignal(int, int, Update)
    signal_download = pyqtSignal(int, int, int, int)

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
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(311)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(120)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.clicked.connect(self.tb_onclike)

        self.signal.connect(self.create_widget_update)
        self.signal_image_download.connect(self.refresh_widget_update)
        self.get_thread = GetListUpdateThread(self.signal)
        self.get_thread.start()
        self.queue_helper = DownloadImageThread(self.signal_image_download)

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
        dialog.ui = Form(data.link)
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def create_widget_update(self, update_list):
        idx = 0
        idy = 0
        self.tableWidget.setRowCount(50)
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
