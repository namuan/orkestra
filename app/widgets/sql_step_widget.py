from PyQt5 import QtWidgets

from app.generated.SqlStepWidget_ui import Ui_SqlStepWidget


class SqlStepWidget(QtWidgets.QWidget, Ui_SqlStepWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
