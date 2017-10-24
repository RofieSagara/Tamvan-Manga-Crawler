# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Infowindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from holder.info import Info
from thread.getinfomangathread import GetInfoMangaThread
from thread.getimagecoverthread import GetImageCoverThread
from tools.inputoutput import InputOutput


class Ui_InfoWindow(QObject):
    signal_info = pyqtSignal(object)
    signal_image = pyqtSignal(str)

    def __init__(self, update=None):
        QObject.__init__(self)
        self.data = update

    def setupUi(self, InfoWindow):
        InfoWindow.setObjectName("InfoWindow")
        InfoWindow.resize(706, 590)
        qpix = QtGui.QPixmap(os.path.join(os.getcwd(), "assets", "load_small.jpg"))
        scene = QtWidgets.QGraphicsScene()
        item = QtWidgets.QGraphicsPixmapItem(qpix)
        scene.addItem(item)
        self.imgCover = QtWidgets.QGraphicsView(scene, InfoWindow)
        self.imgCover.setGeometry(QtCore.QRect(10, 50, 191, 290))
        self.imgCover.setObjectName("imgCover")
        self.lTitle = QtWidgets.QLabel(InfoWindow)
        self.lTitle.setGeometry(QtCore.QRect(10, 10, 681, 31))
        self.lTitle.setObjectName("lTitle")
        self.bDownload = QtWidgets.QPushButton(InfoWindow)
        self.bDownload.setGeometry(QtCore.QRect(590, 20, 100, 20))
        self.bDownload.setObjectName("bDownload")
        self.bDownload.setText("Download")
        self.bDownload.clicked.connect(self.set_download_click)
        self.lRating = QtWidgets.QLabel(InfoWindow)
        self.lRating.setGeometry(QtCore.QRect(220, 50, 471, 17))
        self.lRating.setObjectName("lRating")
        self.lRank = QtWidgets.QLabel(InfoWindow)
        self.lRank.setGeometry(QtCore.QRect(220, 70, 471, 17))
        self.lRank.setObjectName("lRank")
        self.lAlt = QtWidgets.QLabel(InfoWindow)
        self.lAlt.setGeometry(QtCore.QRect(220, 90, 471, 17))
        self.lAlt.setObjectName("lAlt")
        self.lAut = QtWidgets.QLabel(InfoWindow)
        self.lAut.setGeometry(QtCore.QRect(220, 110, 471, 17))
        self.lAut.setObjectName("lAut")
        self.lArt = QtWidgets.QLabel(InfoWindow)
        self.lArt.setGeometry(QtCore.QRect(220, 130, 471, 17))
        self.lArt.setObjectName("lArt")
        self.lGenre = QtWidgets.QLabel(InfoWindow)
        self.lGenre.setGeometry(QtCore.QRect(220, 150, 471, 17))
        self.lGenre.setObjectName("lGenre")
        self.lType = QtWidgets.QLabel(InfoWindow)
        self.lType.setGeometry(QtCore.QRect(220, 170, 471, 17))
        self.lType.setObjectName("lType")
        self.lRelease = QtWidgets.QLabel(InfoWindow)
        self.lRelease.setGeometry(QtCore.QRect(220, 190, 471, 17))
        self.lRelease.setObjectName("lRelease")
        self.lStatus = QtWidgets.QLabel(InfoWindow)
        self.lStatus.setGeometry(QtCore.QRect(220, 210, 471, 17))
        self.lStatus.setObjectName("lStatus")
        self.lSummary = QtWidgets.QLabel()
        self.lSummary.setGeometry(QtCore.QRect(1, 1, 450, 300))
        self.lSummary.setAlignment(QtCore.Qt.AlignTop)
        self.lSummary.setObjectName("lSummary")
        self.lSummary.setWordWrap(True)
        self.scrollArea = QtWidgets.QScrollArea(InfoWindow)
        self.scrollArea.setGeometry(QtCore.QRect(220, 230, 471, 110))
        self.scrollArea.setObjectName("lSa")
        self.scrollArea.setWidget(self.lSummary)

        self.listChapter = QtWidgets.QListWidget(InfoWindow)
        self.listChapter.setGeometry(QtCore.QRect(10, 350, 681, 231))
        self.listChapter.setObjectName("listChapter")
        self.listChapter.clicked.connect(self.set_click_list)

        self.signal_info.connect(self.set_info)
        self.signal_image.connect(self.set_cover)
        self.th_cover = GetImageCoverThread(self.signal_image)
        self.th_info = GetInfoMangaThread(self.signal_info, self.data)
        self.th_info.start()

        self.retranslateUi(InfoWindow)
        QtCore.QMetaObject.connectSlotsByName(InfoWindow)

    def set_click_list(self, click_item):
        modifer = QtWidgets.QApplication.keyboardModifiers()
        if modifer != QtCore.Qt.ShiftModifier:
            self.listChapter.clearSelection()
            self.listChapter.item(click_item.row()).setSelected(True)

    def set_download_click(self, status):
        for n in self.listChapter.selectedIndexes():
            chapter = self.datachapter[n.row()]
            InputOutput.create_file(chapter.link, chapter.title, self.titlemanga)

    def set_info(self, info):
        self.lTitle.setText(info.title)
        self.lRating.setText("Rating :"+info.rating)
        self.lRank.setText("Rank :"+info.rank)
        self.lAlt.setText("Alternative :"+info.alternative)
        self.lAut.setText("Author(s) :"+info.author)
        self.lArt.setText("Artist(s) :"+info.artist)
        self.lGenre.setText("Genre(s) :"+info.genre)
        self.lType.setText("Type :"+info.typemanga)
        self.lRelease.setText("Release :"+info.release)
        self.lStatus.setText("Status :"+info.status)
        self.lSummary.setText("Summary :\n"+info.summary+"\n")
        self.listChapter.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.datachapter = info.chapter
        self.titlemanga = info.title
        for n in info.chapter:
            self.listChapter.addItem(n.title)
        self.th_cover.set_link(info.cover)
        self.th_cover.start()

    def set_cover(self, path):
        qpix = QtGui.QPixmap(path)
        scene = QtWidgets.QGraphicsScene()
        item = QtWidgets.QGraphicsPixmapItem(qpix)
        scene.addItem(item)
        self.imgCover.setScene(scene)

    def retranslateUi(self, InfoWindow):
        _translate = QtCore.QCoreApplication.translate
        InfoWindow.setWindowTitle(_translate("InfoWindow", "MainWindow"))
        self.lTitle.setText(_translate("InfoWindow", "Loading"))
        self.lRating.setText(_translate("InfoWindow", "Rating"))
        self.lRank.setText(_translate("InfoWindow", "Rank"))
        self.lAlt.setText(_translate("InfoWindow", "Alternative"))
        self.lAut.setText(_translate("InfoWindow", "Author(s)"))
        self.lArt.setText(_translate("InfoWindow", "Artist(s)"))
        self.lGenre.setText(_translate("InfoWindow", "Genre(s)"))
        self.lType.setText(_translate("InfoWindow", "Type"))
        self.lRelease.setText(_translate("InfoWindow", "Release"))
        self.lStatus.setText(_translate("InfoWindow", "Status"))
        self.lSummary.setText(_translate("InfoWindow", "Summary"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_InfoWindow("http://mangapark.me/manga/ikusa-x-koi")
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())