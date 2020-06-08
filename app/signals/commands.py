from PyQt5.QtCore import QObject, pyqtSignal


class AppCommands(QObject):
    tool_switched = pyqtSignal(str)
