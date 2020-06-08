from PyQt5.QtCore import QObject, pyqtSignal


class AppEvents(QObject):
    tool_switched = pyqtSignal(str)
    app_started = pyqtSignal()
