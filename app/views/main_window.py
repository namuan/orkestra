import logging
import sys
import traceback
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QMainWindow, qApp

from app.controllers import (
    MainWindowController,
    ToolbarController,
    ConfigController,
    ShortcutController,
    ScratchPadController,
)
from app.generated.MainWindow_ui import Ui_MainWindow
from app.settings import app


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main Window."""

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setUnifiedTitleAndToolBarOnMac(True)

        # Initialise controllers
        self.main_controller = MainWindowController(self, app)
        self.toolbar_controller = ToolbarController(self, app)
        self.config_controller = ConfigController(self, app)
        self.shortcut_controller = ShortcutController(self, app)
        self.scratch_pad_controller = ScratchPadController(self, app)

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
