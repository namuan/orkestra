import logging
import traceback

import sys
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QMainWindow, qApp

from app.controllers import (
    MainWindowController,
    ToolbarController,
    ShortcutController
)
from app.generated.MainWindow_ui import Ui_MainWindow
from app.sections.environment import EnvironmentView
from app.sections.folder import FoldersView
from app.sections.scratchpad import ScratchPadController
from app.sections.step import StepListView, StepSwitcherController
from app.settings.app_world import AppWorld
from app.views import ConfigurationDialog


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

        # Initialise components
        self.toolbar_controller.init_items()
        self.shortcut_controller.init_items()

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

    def replace_widget(self, selected_widget):
        logging.info("Switching Layout for {}".format(selected_widget))
        self.clear_layout(self.toolWidgetLayout)
        self.toolWidgetLayout.addWidget(selected_widget)

    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            widget_item = layout.takeAt(i)
            if widget_item:
                widget_item.widget().deleteLater()
