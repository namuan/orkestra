from PyQt5 import QtWidgets

from app.generated.HttpStepWidget_ui import Ui_HttpStepWidget


class HttpStepWidget(QtWidgets.QWidget, Ui_HttpStepWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
