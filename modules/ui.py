import sys
from PyQt5.QtWidgets import *

class main_window(QMainWindow):
    def __init__(self):
        cls = type(self)
        if not hasattr(cls, "_init"):
            print("__init__ is called\n")
            super().__init__()
            self.setGeometry(100, 200, 300, 400)
            cls._init = True
         

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            print("__new__ is called\n")
            cls._instance = super().__new__(cls)

            return cls._instance

def get_window():
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    app.exec_()
