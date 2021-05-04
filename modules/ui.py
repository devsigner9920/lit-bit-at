import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

from modules import market
from modules import bull

main_form_class = uic.loadUiType("ui/main_window.ui")[0]
bull_form_class = uic.loadUiType("ui/bull_window.ui")[0]


class main_window(QMainWindow, main_form_class):
    def __init__(self):
        super(main_window, self).__init__()
        self.setupUi(self)
        # self.setGeometry(100, 200, 300, 400)
        # self.setWindowTitle("lit bit")
        self.btn_bull.clicked.connect(self.open_bull_window)

        markets = market.get_market()
        bull_list = []
        for mk in markets:
            bull_list.append(bull.get_bull(mk['market']))

        self.tbl_bull.setRowCount(len(bull_list))

        timer = QTimer(self)
        timer.start(5000)
        timer.timeout.connect(self.timeout)

    @pyqtSlot()
    def open_bull_window(self):
        # QStackedWidget.setCurrentIndex(QStackedWidget.currentIndex() + 1)
        print("test?!")

    def timeout(self):
        print("5초에요!!")


class bull_window(QDialog, bull_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.setGeometry(100, 200, 300, 400)
        # self.setWindowTitle("lit bit")


def get_window():
    app = QApplication(sys.argv)

    # layout instance
    main = main_window()
    bull = bull_window()

    main.show()

    app.exec_()
