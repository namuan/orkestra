from PyQt5.QtCore import QObject, pyqtSignal


class DataEvents(QObject):
    step_added = pyqtSignal(str)  # StepEntity.id
    steps_deleted = pyqtSignal()
    step_deleted = pyqtSignal(str)  # StepEntity.id
    step_selection_changed = pyqtSignal(str)  # Newly selected StepEntity.id
    environments_changed = pyqtSignal()
    environment_selection_changed = pyqtSignal(str)  # Newly selected environment name
