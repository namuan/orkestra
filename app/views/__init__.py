from PyQt5.QtWidgets import QFileDialog

from .configuration_dialog import ConfigurationDialog
from .folders_view import FoldersView


def open_file_dialog(parent, dialog_title, dialog_location, file_filter=None):
    return QFileDialog.getOpenFileName(
        parent, dialog_title, dialog_location, filter=file_filter
    )
