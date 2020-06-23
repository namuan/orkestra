import logging
import logging.handlers
from pathlib import Path
from typing import Any, Union

from PyQt5.QtCore import QSettings, QStandardPaths
from PyQt5.QtWidgets import qApp

from app.data.app_state import AppStateStore
from app.data.data_store import DataStore
from app.sections.configuration.app_config import AppConfig
from app.sections.environment.environment_store import EnvironmentStore
from app.sections.folder import FolderStore
from app.sections.step.step_store import StepStore
from app.utils.str_utils import str_to_bool


class AppWorld:
    settings: QSettings
    app_dir: Union[Path, Any]
    app_name: str
    data: DataStore
    app_state_store: AppStateStore
    folder_store: FolderStore
    step_store: StepStore
    environment_store: EnvironmentStore

    def __init__(self):
        self.docs_location: Path = Path(
            QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        )

    def init(self):
        self.app_name = qApp.applicationName().lower()
        self.app_dir = Path(
            QStandardPaths.writableLocation(QStandardPaths.AppConfigLocation)
        )
        self.app_dir.mkdir(exist_ok=True)
        settings_file = f"{self.app_name}.ini"
        self.settings = QSettings(
            self.app_dir.joinpath(settings_file).as_posix(), QSettings.IniFormat
        )
        self.settings.sync()
        self.data = DataStore(self.app_dir)
        self.app_state_store = AppStateStore(self.data)
        self.folder_store = FolderStore(self.data)
        self.step_store = StepStore(self.data)
        self.environment_store = EnvironmentStore(self.data)

    def init_logger(self):
        log_file = f"{self.app_name}.log"
        handlers = [
            logging.handlers.RotatingFileHandler(
                self.app_dir.joinpath(log_file), maxBytes=1000000, backupCount=1
            ),
            logging.StreamHandler(),
        ]

        # noinspection PyArgumentList
        logging.basicConfig(
            handlers=handlers,
            format="%(asctime)s - %(filename)s:%(lineno)d - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            level=logging.DEBUG,
        )
        logging.captureWarnings(capture=True)

    def save_window_state(self, geometry, window_state):
        self.settings.setValue("geometry", geometry)
        self.settings.setValue("windowState", window_state)
        self.settings.sync()

    def save_configuration(self, app_config):
        self.settings.setValue(AppConfig.STARTUP_CHECK_KEY, app_config.startup_check)
        self.settings.sync()

    def load_configuration(self):
        app_config = AppConfig()
        settings_value = self.settings.value(
            AppConfig.STARTUP_CHECK_KEY, app_config.startup_check
        )
        app_config.startup_check = str_to_bool(settings_value)
        return app_config

    def geometry(self):
        return self.settings.value("geometry", None)

    def window_state(self):
        return self.settings.value("windowState", None)

    def started(self):
        self.data.events.app_started.emit()
