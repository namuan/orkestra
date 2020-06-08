from app.controllers.folders_controller import FoldersController


class FoldersView:
    def __init__(self, parent):
        self.parent = parent
        self.controller = FoldersController(self, self.parent.world)

    def on_update_folders(self, folders):
        for folder in folders:
            self.parent.cmb_folders.addItem(folder.name)
