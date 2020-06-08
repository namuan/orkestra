from app.controllers.folders_controller import FoldersController
from app.settings import app


class FoldersView:
    def __init__(self, parent):
        self.parent = parent
        self.controller = FoldersController(self, app)

    def on_update_folders(self):
        print("Do something with self.parent.combobox")
