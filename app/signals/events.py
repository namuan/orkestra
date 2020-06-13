from PyQt5.QtCore import QObject, pyqtSignal


class AppEvents(QObject):
    app_started = pyqtSignal()
    step_added = pyqtSignal(str)  # StepEntity.id
    step_selection_changed = pyqtSignal(str)  # Newly selected StepEntity.id
    environments_added = pyqtSignal()
