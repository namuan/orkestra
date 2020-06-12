from PyQt5.QtWidgets import QFileDialog

from .configuration_dialog import ConfigurationDialog
from .environment_view import EnvironmentView
from .folders_view import FoldersView
from .step_list_view import StepListView


def open_file_dialog(parent, dialog_title, dialog_location, file_filter=None):
    return QFileDialog.getOpenFileName(
        parent, dialog_title, dialog_location, filter=file_filter
    )
