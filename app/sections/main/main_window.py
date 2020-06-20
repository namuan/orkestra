import logging
import traceback

import sys
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QMainWindow, qApp

from app.core.step_types import StepType
from app.generated.MainWindow_ui import Ui_MainWindow
from app.sections.configuration import ConfigurationDialog
from app.sections.environment import EnvironmentView
from app.sections.folder import FoldersView
from app.sections.scratchpad import ScratchPadController
from app.sections.shortcut import ShortcutController
from app.sections.step.step_list_view import StepListView
from app.sections.step.step_switcher_controller import StepSwitcherController
from app.sections.toolbar import ToolbarController
from app.sections.toolbar.environment_list_view import EnvironmentListView
from app.settings.app_world import AppWorld
from app.widgets.http_step_widget import HttpStepWidget
from app.widgets.sql_step_widget import SqlStepWidget
from .main_controller import MainWindowController


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main Window."""

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setUnifiedTitleAndToolBarOnMac(True)

        self.world = AppWorld()

        # Initialise controllers
        self.main_controller = MainWindowController(self)
        self.toolbar_controller = ToolbarController(self)
        self.shortcut_controller = ShortcutController(self)
        self.scratch_pad_controller = ScratchPadController(self)
        self.step_switcher_controller = StepSwitcherController(self)

        # Initialise Sub-Views
        self.config_view = ConfigurationDialog(self)
        self.folders_view = FoldersView(self)
        self.step_list_view = StepListView(self)
        self.environment_view = EnvironmentView(self)
        self.environment_list_view = EnvironmentListView(self)

        # Initialise components
        self.toolbar_controller.init_items()
        self.shortcut_controller.init_items()

        # Initialise stacks
        self.http_step_widget = HttpStepWidget()
        self.sql_step_widget = SqlStepWidget()

        self.stackedWidget.addWidget(self.http_step_widget)
        self.stackedWidget.addWidget(self.sql_step_widget)

        # Initialise Sub-Systems
        sys.excepthook = MainWindow.log_uncaught_exceptions

        # Main Window events

    def resizeEvent(self, event):
        self.main_controller.after_window_loaded()

    @staticmethod
    def log_uncaught_exceptions(cls, exc, tb) -> None:
        logging.critical("".join(traceback.format_tb(tb)))
        logging.critical("{0}: {1}".format(cls, exc))

    def closeEvent(self, event: QCloseEvent):
        logging.info("Received close event")
        event.accept()
        self.main_controller.shutdown()
        try:
            qApp.exit(0)
        except:
            pass

    def replace_step(self, new_step):
        logging.info("Switching Layout to {}".format(new_step))
        if new_step.step_type == StepType.HTTP:
            self.stackedWidget.setCurrentWidget(self.http_step_widget)
        elif new_step.step_type == StepType.SQL:
            self.stackedWidget.setCurrentWidget(self.sql_step_widget)
