class FoldersController:
    def __init__(self, main_window, world):
        self.main_window = main_window
        self.world = world

        # ui events
        self.world.data.events.app_started.connect(self.on_app_started)

    def on_app_started(self):
        folders = self.world.folder_store.folders.folders
        selected_folder = next((folder for folder in folders if folder.selected), None)
        self.main_window.on_update_folders(folders, selected_folder)
