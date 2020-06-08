from PyQt5 import QtCore
from PyQt5.QtCore import QObject, QEvent

from app.settings.app_world import AppWorld


class ScratchPadEvents(QObject):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.parent = parent
        self.app = app

    def eventFilter(self, source: QObject, event: QEvent):
        if event.type() == QtCore.QEvent.FocusOut:
            self.save_scratch_pad()

        return super().eventFilter(source, event)

    def save_scratch_pad(self):
        scratch = self.parent.txt_scratch_pad.toPlainText()
        self.app.app_state_store.update_scratch_note(scratch)


class ScratchPadController:
    def __init__(self, parent, app: AppWorld):
        self.parent = parent
        self.app = app
        self.events = ScratchPadEvents(self.parent, self.app)

        # installing event filter
        self.parent.txt_scratch_pad.installEventFilter(self.events)

    def init(self):
        scratch_note = self.app.app_state_store.get_scratch_note()
        self.parent.txt_scratch_pad.setPlainText(scratch_note)
