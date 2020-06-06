from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QToolBar,
    QWidget,
    QSizePolicy,
    QAction,
)


class ToolbarController:
    def __init__(self, parent_window, app):
        self.parent = parent_window
        self.toolbar = QToolBar()
        self.app = app
        self.populating_tools = True

    def init(self):
        pass

    def init_items(self):
        self.toolbar.setObjectName("maintoolbar")
        self.parent.addToolBar(Qt.TopToolBarArea, self.toolbar)
        self.toolbar.setMovable(False)

        self.toolbar.addSeparator()

        spacer = QWidget(self.parent)
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.toolbar.addWidget(spacer)

        toolbar_configure_action = QAction(
            QIcon(":/images/configure-48.png"), "Settings", self.parent
        )
        toolbar_configure_action.triggered.connect(
            self.parent.config_controller.show_dialog
        )
        self.toolbar.addAction(toolbar_configure_action)
