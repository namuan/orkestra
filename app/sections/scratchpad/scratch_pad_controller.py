from PyQt5 import QtCore
from PyQt5.QtCore import QObject, QEvent


class ScratchPadEvents(QObject):
    def __init__(self, main_window, app):
        super().__init__(main_window)
        self.main_window = main_window
        self.app = app

    def eventFilter(self, source: QObject, event: QEvent):
        if event.type() == QtCore.QEvent.FocusOut:
            self.save_scratch_pad()

        return super().eventFilter(source, event)

    def save_scratch_pad(self):
        scratch = self.main_window.txt_scratch_pad.toPlainText()
        self.app.app_state_store.update_scratch_note(scratch)


class ScratchPadController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.world = self.main_window.world
        self.events = ScratchPadEvents(self.main_window, self.world)

        # ui events
        self.world.events.app_started.connect(self.on_app_started)

        # installing event filter
        self.main_window.txt_scratch_pad.installEventFilter(self.events)

    def on_app_started(self):
        scratch_note = self.world.app_state_store.get_scratch_note()
        self.main_window.txt_scratch_pad.setPlainText(scratch_note)
