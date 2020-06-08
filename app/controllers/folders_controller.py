from app.settings.app_world import AppWorld


class FoldersController:
    def __init__(self, view, app: AppWorld):
        self.view = view
        self.app = app

        # ui events
        self.app.data.events.app_started.connect(self.on_app_started)

    def on_app_started(self):
        folders = self.app.folder_store.folders.folders
        self.view.on_update_folders(folders)
