import logging
import sys
import traceback
from pathlib import Path

from PyQt6.QtCore import QDir
from PyQt6.QtGui import QCloseEvent
from PyQt6.QtWidgets import QMainWindow, QApplication

from app.core.step_types import StepType
from app.generated.MainWindow_ui import Ui_MainWindow
from app.sections.configuration import ConfigurationDialog
from app.sections.environment import EnvironmentView
from app.sections.folder import FoldersView
from app.sections.scratchpad import ScratchPadController
from app.sections.shortcut import ShortcutController
from app.sections.sqlstep.sql_step_view import SqlStepView
from app.sections.step.step_list_view import StepListView
from app.sections.step.step_switcher_controller import StepSwitcherController
from app.sections.toolbar import ToolbarController
from app.sections.toolbar.environment_list_view import EnvironmentListView
from app.settings.app_world import AppWorld
from .default_page_controller import DefaultPageController
from .main_controller import MainWindowController
from ..httpstep.http_step_view import HttpStepView


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main Window."""

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setUnifiedTitleAndToolBarOnMac(True)

        self.world = AppWorld()

        resources_path = (Path(__file__).parent.parent.parent.parent / "resources")
        QDir.addSearchPath('icons', resources_path.joinpath("images").as_posix())

        # Initialise controllers
        self.main_controller = MainWindowController(self)
        self.toolbar_controller = ToolbarController(self)
        self.shortcut_controller = ShortcutController(self)
        self.scratch_pad_controller = ScratchPadController(self)
        self.step_switcher_controller = StepSwitcherController(self)
        self.default_page_controller = DefaultPageController(self)

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
        # self.http_step_widget = HttpStepWidget()
        self.sql_step_view = SqlStepView(self)
        self.http_step_view = HttpStepView(self)

        self.stackedWidget.addWidget(self.http_step_view)
        self.stackedWidget.addWidget(self.sql_step_view)

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
            QApplication.instance().exit(0)
        except:
            pass

    def replace_step(self, new_step):
        logging.info("Switching Layout to {}".format(new_step))
        if not new_step:
            self.stackedWidget.setCurrentIndex(0)
        elif new_step.step_type == StepType.HTTP:
            self.stackedWidget.setCurrentWidget(self.http_step_view)
        elif new_step.step_type == StepType.SQL:
            self.stackedWidget.setCurrentWidget(self.sql_step_view)
