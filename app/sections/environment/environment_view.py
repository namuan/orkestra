import logging

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog

from app.generated.EnvironmentDialog_ui import Ui_EnvironmentsDialog
from .environment_controller import EnvironmentController


class EnvironmentView(QDialog, Ui_EnvironmentsDialog):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.setupUi(self)
        self.setup_button_icons()

        self.controller = EnvironmentController(self, main_window.world)

    def show_dialog(self):
        self.show()

    def remove_selected_environment_widget(self):
        selected_row = self.lst_environments.currentRow()
        if selected_row < 0:
            return

        logging.info("Removing environment widget at {}".format(selected_row))
        self.lst_environments.takeItem(selected_row)

    def add_new_environment_widget(self, env_name):
        logging.info("Adding new environment widget for {}".format(env_name))
        item = QtWidgets.QListWidgetItem()
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        item.setText(env_name)
        self.lst_environments.addItem(item)
        self.select_new_environment_widget()

    def select_new_environment_widget(self):
        self.lst_environments.setCurrentRow(self.lst_environments.count() - 1)

    def setup_button_icons(self):
        self.btn_add_environment.setIcon(self._icon_with(":/images/plus-48.png"))
        self.btn_remove_environment.setIcon(self._icon_with(":/images/minus-48.png"))

    @staticmethod
    def _icon_with(image_resource):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(image_resource), QtGui.QIcon.Normal)
        return icon