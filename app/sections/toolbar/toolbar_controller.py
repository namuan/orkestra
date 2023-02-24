import logging
from functools import partial

from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QToolBar,
    QWidget,
    QSizePolicy,
    QComboBox,
    QWidgetAction,
)
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication

from app.core.constants import HTTP_STEP, SQL_STEP
from app.settings.app_world import AppWorld


class ToolbarController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.toolbar = QToolBar()
        self.world: AppWorld = self.main_window.world

        # app start events
        self.world.events.app_started.connect(self.on_app_started)

    def on_app_started(self):
        pass

    def init_items(self):
        self.toolbar.setObjectName("main_toolbar")
        self.main_window.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)
        self.toolbar.setMovable(False)

        toolbar_http_step_action = QAction(
            QIcon("icons:http-48.png"), "Http Step", self.main_window
        )
        toolbar_http_step_action.triggered.connect(
            partial(
                self.main_window.default_page_controller.trigger_add_step_command,
                HTTP_STEP,
            )
        )
        self.toolbar.addAction(toolbar_http_step_action)

        toolbar_sql_step_action = QAction(
            QIcon("icons:sql-48.png"), "Sql Step", self.main_window
        )
        toolbar_sql_step_action.triggered.connect(
            partial(
                self.main_window.default_page_controller.trigger_add_step_command,
                SQL_STEP,
            )
        )
        self.toolbar.addAction(toolbar_sql_step_action)

        self.toolbar.addSeparator()

        toolbar_environment_action = QAction(
            QIcon("icons:environment-48.png"),
            "Configure Environments",
            self.main_window,
        )
        toolbar_environment_action.triggered.connect(
            self.main_window.environment_view.show_dialog
        )
        self.toolbar.addAction(toolbar_environment_action)

        tool_bar_envs_list = QComboBox(self.main_window)
        tool_bar_envs_list.setSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding
        )
        tool_bar_envs_list.setDuplicatesEnabled(False)
        tool_bar_envs_list.currentTextChanged.connect(
            self.main_window.environment_list_view.on_toolbar_selected_environment_changed
        )
        tool_bar_envs_list_action = QWidgetAction(self.main_window)
        tool_bar_envs_list_action.setText("Environmnents")
        tool_bar_envs_list_action.setDefaultWidget(tool_bar_envs_list)
        self.toolbar.addAction(tool_bar_envs_list_action)

        self.toolbar.addSeparator()

        spacer = QWidget(self.main_window)
        spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.toolbar.addWidget(spacer)

        toolbar_configure_action = QAction(
            QIcon("icons:configure-48.png"), "Settings", self.main_window
        )
        toolbar_configure_action.triggered.connect(
            self.main_window.config_view.show_dialog
        )
        self.toolbar.addAction(toolbar_configure_action)

        toolbar_quit_action = QAction(
            QIcon("icons:quit-48.png"), "Quit", self.main_window
        )
        toolbar_quit_action.triggered.connect(self.trigger_quit_application)
        self.toolbar.addAction(toolbar_quit_action)

    def trigger_quit_application(self):
        QApplication.instance().quit()
