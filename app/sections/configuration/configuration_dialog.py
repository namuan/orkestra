from PyQt6.QtWidgets import QDialog

from app.generated.ConfigurationDialog_ui import Ui_Configuration
from .config_controller import ConfigController


class ConfigurationDialog(QDialog, Ui_Configuration):
    def __init__(self, main_window):
        super(ConfigurationDialog, self).__init__(main_window)
        self.setupUi(self)
        self.controller = ConfigController(self, main_window.world)

    def show_dialog(self):
        self.controller.show_dialog()
