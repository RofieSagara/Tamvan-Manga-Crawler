from custom.widgetupdate import WidgetUpdate
from thread.downloadimagethread import DownloadImageThread
from view.infowindow import Ui_InfoWindow as Form
from PyQt5 import QtCore, QtGui, QtWidgets
from custom.qscreen import QScene
import os


def set_prog(self, frm, total, max_image, now_image):
    print(frm,total,max_image,now_image)
    self.prog.setMaximum(max_image)
    self.prog.setValue(now_image)
    self.prog.setFormat("Downloading Image (" + str(now_image) + "/" + str(max_image) + ") %p%")
    if total == frm and max_image == now_image:
        self.status.setText("Waiting. . .")
        self.prog.setFormat("")
        self.prog.setMaximum(0)
        self.prog.setMinimum(0)
        self.prog.setValue(0)
    else:
        self.status.setText("still " + str(total) + " Chapter left")


def button_update_onclick(self):
    self.signal_image_download_update.connect(self.refresh_widget_update)
    self.queue_helper = DownloadImageThread(self.signal_image_download_update)
    self.thread_update.start()


def button_browser_onclick(self):
    self.signal_image_download_browser.connect(self.refresh_image_browser)
    self.queue_helper = DownloadImageThread(self.signal_image_download_browser)
    self.thread_browser.start()


def get_browser_more(self):
    self.thread_browser.get_next()
    self.thread_browser.start()


def create_widget_browser(self, search_list):

    if self.tableWidget.lidx == 0 and self.tableWidget.lidy == 0:
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        self.tableWidget.clear()
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(155)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(220)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        idx = 0
        idy = 0
    else:
        idx = self.tableWidget.lidx
        idy = self.tableWidget.lidy+1
        if idy >= 3:
            idy = 0
            idx += 1
    # self.tableWidget = QtWidgets.QTableWidget()
    # self.tableWidget.verticalScrollBar()
    for n in search_list:
        wUpdate = WidgetUpdate()
        wUpdate.setGeometry(QtCore.QRect(0, 0, 155, 220))
        wUpdate.setAutoFillBackground(True)
        wUpdate.setObjectName("wUpdate")
        wUpdate.tag = n
        qpix = QtGui.QPixmap(os.path.join(os.getcwd(), "assets", "load_small.jpg"))
        scene = QtWidgets.QGraphicsScene()
        item = QtWidgets.QGraphicsPixmapItem(qpix)
        scene.addItem(item)
        imgCover = QtWidgets.QGraphicsView(scene, wUpdate)
        imgCover.setGeometry(QtCore.QRect(10, 10, 130, 190))
        imgCover.setObjectName("imgCover")
        lTitle = QtWidgets.QLabel(wUpdate)
        lTitle.setGeometry(QtCore.QRect(10, 160, 141, 51))
        lTitle.setObjectName("lTitle")
        lTitle.setText(n.title)
        lTitle.setWordWrap(True)
        lTitle.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        lTitle.setStyleSheet("background-color: rgba(255, 255, 255, 200)")
        self.tableWidget.setCellWidget(idx, idy, wUpdate)
        self.tableWidget.set_last_idx_idy(idx=idx, idy=idy)
        self.queue_helper.add(idx, idy, n)
        if idy >= 3:
            idy = 0
            idx += 1
            self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
        else:
            idy += 1
    self.queue_helper.start()
    print(self.tableWidget.lidx, " and ", self.tableWidget.lidy)


def refresh_image_browser(self, x, y, update_item):
    w_update = WidgetUpdate()
    w_update.setGeometry(QtCore.QRect(0, 0, 155, 220))
    w_update.setAutoFillBackground(True)
    w_update.setObjectName("wUpdate")
    w_update.tag = update_item
    p = w_update.palette()
    p.setColor(w_update.backgroundRole(), QtCore.Qt.red)
    w_update.setPalette(p)
    qpix = QtGui.QPixmap(update_item.small_cover_local)
    if not qpix.isNull():
        qpix = qpix.scaled(120, 180)
    else:
        qpix = QtGui.QPixmap(os.path.join(os.getcwd(), "assets", "error_small.jpg"))
        qpix = qpix.scaled(130, 190)
    scene = QScene(idx=x, obj=self, idy=y)
    item = QtWidgets.QGraphicsPixmapItem(qpix)
    img_cover = QtWidgets.QGraphicsView(scene, w_update)
    img_cover.setGeometry(QtCore.QRect(10, 10, 130, 190))
    img_cover.setObjectName("imgCover")
    scene.addItem(item)
    l_title = QtWidgets.QLabel(w_update)
    l_title.setGeometry(QtCore.QRect(10, 160, 141, 51))
    l_title.setObjectName("lTitle")
    l_title.setText(update_item.title)
    l_title.setWordWrap(True)
    l_title.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
    l_title.setStyleSheet("background-color: rgba(255, 255, 255, 200)")
    self.tableWidget.removeCellWidget(x, y)
    self.tableWidget.setCellWidget(x, y, w_update)
    img_cover.show()


def tb_onclike(self, clicked_index, alt_index=None, alt_colu=None):
    print(type(clicked_index))
    print(type(clicked_index.row()))
    if clicked_index.row() == -1:
        row = alt_index
        colum = alt_colu
    else:
        row = clicked_index.row()
        colum = clicked_index.column()
    data = self.tableWidget.cellWidget(row, colum).tag
    print("Select :" + data.title)
    print("Position :row(" + str(row) + ") col(" + str(colum) + ")")
    dialog = QtWidgets.QDialog()
    link = data.link
    if "mangapark" in link:
        dialog.ui = Form(data.link)
    else:
        dialog.ui = Form("http://mangapark.me/" + data.link)
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
    scene = QScene(idx=x, obj=self, idy=y)
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
