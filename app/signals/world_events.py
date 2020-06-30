from PyQt5.QtCore import QObject, pyqtSignal

from app.commands.run_step_command import RunStepCommand


class WorldEvents(QObject):
    worker_started = pyqtSignal(RunStepCommand)
    app_started = pyqtSignal()
