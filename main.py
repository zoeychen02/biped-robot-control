import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, QtCore
from main_window import Ui_MainWindow
from robot import Robot
from custom_init import CustomInit

if __name__ == '__main__':
    QtGui.QGuiApplication.setAttribute(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    window = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(window)
    c_init = CustomInit(ui)
    rbot = Robot(ui)

    window.show()
    sys.exit(app.exec())
