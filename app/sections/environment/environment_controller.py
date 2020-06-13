from app.core.random_utils import random_environment


class EnvironmentController:
    def __init__(self, parent, world):
        self.parent = parent
        self.world = world

        # ui events
        self.parent.btn_add_environment.pressed.connect(self.trigger_add_environment)
        self.parent.btn_remove_environment.pressed.connect(self.trigger_remove_environment)
        self.parent.btn_dialog_close.accepted.connect(self.trigger_save_changes)
        self.parent.lst_environments.itemChanged.connect(self.trigger_current_item_changed)

    def trigger_current_item_changed(self, list_item):
        pass

    def trigger_add_environment(self):
        random_environment_name = random_environment()
        self.parent.add_new_environment_widget(random_environment_name)

    def trigger_remove_environment(self):
        self.parent.remove_selected_environment_widget()

    def trigger_save_changes(self):
        environments = [
            self.parent.lst_environments.item(i).text()
            for i in range(self.parent.lst_environments.count())
        ]
        self.world.environment_store.upsert_environments(environments)
