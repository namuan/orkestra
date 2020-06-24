from PyQt5 import QtWidgets

from app.generated.SqlStepWidget_ui import Ui_SqlStepWidget


class SqlStepView(QtWidgets.QWidget, Ui_SqlStepWidget):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.setupUi(self)
