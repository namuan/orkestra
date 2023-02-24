import logging

from PyQt6.QtCore import QThread, pyqtSlot


class WorkerThread(QThread):
    def __init__(self, world, wrapped_command):
        super().__init__()
        self.world = world
        self.run_step_command = wrapped_command.run_step_command

    @pyqtSlot()
    def run(self):
        logging.info(
            "Running WorkerThread for RunStepCommand: {}".format(self.run_step_command)
        )
        self.world.events.worker_started.emit(self.run_step_command)
        import time

        time.sleep(5)
        self.world.events.worker_stopped.emit()
