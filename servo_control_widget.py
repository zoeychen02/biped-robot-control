from PyQt5.QtWidgets import QWidget

from servo_control_layout import Ui_Form


class ServoControl(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
