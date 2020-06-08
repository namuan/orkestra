from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QToolBar,
    QWidget,
    QSizePolicy,
    QAction,
)

from app.settings.app_world import AppWorld


class ToolbarController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.toolbar = QToolBar()
        self.world: AppWorld = self.main_window.world
        self.populating_tools = True

        # ui events
        self.world.data.events.app_started.connect(self.on_app_started)

    def on_app_started(self):
        pass

    def init_items(self):
        self.toolbar.setObjectName("main_toolbar")
        self.main_window.addToolBar(Qt.TopToolBarArea, self.toolbar)
        self.toolbar.setMovable(False)

        self.toolbar.addSeparator()

        spacer = QWidget(self.main_window)
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.toolbar.addWidget(spacer)

        toolbar_configure_action = QAction(
            QIcon(":/images/configure-48.png"), "Settings", self.main_window
        )
        toolbar_configure_action.triggered.connect(
            self.main_window.config_view.show_dialog
        )
        self.toolbar.addAction(toolbar_configure_action)
