from PyQt5.QtWidgets import QDialog

from app.generated.EnvironmentDialog_ui import Ui_EnvironmentsDialog


class EnvironmentView(QDialog, Ui_EnvironmentsDialog):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.setupUi(self)

    def show_dialog(self):
        self.show()
