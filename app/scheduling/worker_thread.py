import logging

from PyQt5.QtCore import QThread, pyqtSlot


class WorkerThread(QThread):
    def __init__(self, wrapped_command):
        super().__init__()
        self.run_step_command = wrapped_command.run_step_command

    @pyqtSlot()
    def run(self):
        logging.info("Running WorkerThread for RunStepCommand: {}".format(self.run_step_command))
