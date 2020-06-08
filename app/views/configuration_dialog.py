from PyQt5.QtWidgets import QDialog

from app.controllers import ConfigController
from app.generated.ConfigurationDialog_ui import Ui_Configuration


class ConfigurationDialog(QDialog, Ui_Configuration):
    def __init__(self, main_window):
        super(ConfigurationDialog, self).__init__(main_window)
        self.setupUi(self)
        self.controller = ConfigController(self, main_window.world)

    def show_dialog(self):
        self.controller.show_dialog()
