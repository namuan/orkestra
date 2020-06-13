import logging
from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QToolBar,
    QWidget,
    QSizePolicy,
    QAction,
    QMenu,
)

from app.commands.add_step_command import AddStepCommand
from app.core.constants import AVAILABLE_STEPS
from app.core.step_types import StepType
from app.settings.app_world import AppWorld


class ToolbarController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.toolbar = QToolBar()
        self.world: AppWorld = self.main_window.world

        # ui events
        self.world.data.events.app_started.connect(self.on_app_started)

    def on_app_started(self):
        pass

    def init_items(self):
        self.toolbar.setObjectName("main_toolbar")
        self.main_window.addToolBar(Qt.TopToolBarArea, self.toolbar)
        self.toolbar.setMovable(False)

        steps_menu = QMenu()
        for step in AVAILABLE_STEPS:
            s_action = QAction(step, self.main_window)
            s_action.triggered.connect(partial(self.trigger_add_step_command, step))
            steps_menu.addAction(s_action)

        toolbar_new_step_action = QAction(
            QIcon(":/images/plus-48.png"), "New Step", self.main_window
        )
        toolbar_new_step_action.setMenu(steps_menu)
        self.toolbar.addAction(toolbar_new_step_action)

        self.toolbar.addSeparator()

        toolbar_environment_action = QAction(
            QIcon(":/images/environment-48.png"),
            "Configure Environments",
            self.main_window,
        )
        toolbar_environment_action.triggered.connect(self.main_window.environment_view.show_dialog)
        self.toolbar.addAction(toolbar_environment_action)

        # TODO: Add a combo box for displaying environments

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

    def trigger_add_step_command(self, step_name):
        add_step_command = AddStepCommand(step_type=StepType[step_name])
        logging.info("Adding new step: {}".format(add_step_command))
        self.world.step_store.add_step(add_step_command)
