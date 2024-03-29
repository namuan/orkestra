from PyQt6.QtCore import QObject, pyqtSignal

from app.commands.run_step_command import RunStepCommand


class WorldEvents(QObject):
    worker_started = pyqtSignal(RunStepCommand)
    worker_stopped = pyqtSignal()
    app_started = pyqtSignal()
