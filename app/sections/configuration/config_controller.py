from .app_config import AppConfig


class ConfigController:
    def __init__(self, parent, world):
        self.parent = parent
        self.world = world

        # ui events
        self.parent.btn_save_configuration.pressed.connect(self.on_success)
        self.parent.btn_cancel_configuration.pressed.connect(self.ignore_changes)

    def ignore_changes(self):
        self.parent.reject()

    def on_success(self):
        app_config = self.form_to_object()
        self.world.save_configuration(app_config)
        self.parent.accept()

    def show_dialog(self):
        app_config = self.world.load_configuration()
        self.object_to_form(app_config)
        self.parent.show()

    def form_to_object(self):
        config = AppConfig()
        config.startup_check = self.parent.chk_updates_startup.isChecked()
        return config

    def object_to_form(self, app_config: AppConfig):
        self.parent.chk_updates_startup.setChecked(app_config.startup_check)
