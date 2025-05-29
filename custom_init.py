import PyQt5.QtCore
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt

from main_window import Ui_MainWindow


class CustomInit:
    def __init__(self, app_ui: Ui_MainWindow):
        self.app_ui = app_ui
        self.initConnect()
        self.setupUi()
        self.servo_list = [self.app_ui.widget_1, self.app_ui.widget_2, self.app_ui.widget_3, self.app_ui.widget_4,
                           self.app_ui.widget_5, self.app_ui.widget_6, self.app_ui.widget_7, self.app_ui.widget_8,
                           self.app_ui.widget_9, self.app_ui.widget_10, self.app_ui.widget_11, self.app_ui.widget_12]

    def initConnect(self):
        self.app_ui.pushButton_2.clicked.connect(self.record)

    def setupUi(self):
        self.app_ui.widget_1.ui.label.setText('舵机0')
        self.app_ui.widget_2.ui.label.setText('舵机1')
        self.app_ui.widget_3.ui.label.setText('舵机2')
        self.app_ui.widget_4.ui.label.setText('舵机3')
        self.app_ui.widget_5.ui.label.setText('舵机4')
        self.app_ui.widget_6.ui.label.setText('舵机5')
        self.app_ui.widget_7.ui.label.setText('舵机6')
        self.app_ui.widget_8.ui.label.setText('舵机7')
        self.app_ui.widget_9.ui.label.setText('舵机8')
        self.app_ui.widget_10.ui.label.setText('舵机9')
        self.app_ui.widget_11.ui.label.setText('舵机10')
        self.app_ui.widget_12.ui.label.setText('舵机11')

    def record(self):
        current_row = self.app_ui.tableWidget.rowCount()
        self.app_ui.tableWidget.insertRow(current_row)
        for i in range(12):
            val = self.servo_list[i].ui.doubleSpinBox.value()
            newItem = QTableWidgetItem(f'{val}')
            self.app_ui.tableWidget.setItem(current_row, i, newItem)
            self.app_ui.tableWidget.item(current_row, i).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
