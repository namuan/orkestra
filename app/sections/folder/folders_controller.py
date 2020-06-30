class FoldersController:
    def __init__(self, parent_view, world):
        self.parent_view = parent_view
        self.world = world

        # domain events
        self.world.events.app_started.connect(self.on_app_started)

    def on_app_started(self):
        folders = self.world.folder_store.folders.folders
        selected_folder = next((folder for folder in folders if folder.selected), None)
        self.parent_view.on_update_folders(folders, selected_folder)
