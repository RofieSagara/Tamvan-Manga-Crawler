import unittest
from tools.inputoutput import InputOutput
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from infowindow import Ui_InfoWindow
from core.mangapark import MangaPark
from holder.update import Update
from infowindow import Ui_InfoWindow as Form


class MyTestCase(unittest.TestCase):

    def test_download(self):
        list = InputOutput.read_all_file()
        print(list)


if __name__ == '__main__':
    unittest.main()
