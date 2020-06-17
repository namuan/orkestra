from app.core.random_utils import random_environment


class EnvironmentController:
    def __init__(self, parent, world):
        self.parent = parent
        self.world = world
        self.loading_environments = False

        # ui events
        self.parent.btn_add_environment.pressed.connect(self.trigger_add_environment)
        self.parent.btn_remove_environment.pressed.connect(
            self.trigger_remove_environment
        )
        self.parent.btn_dialog_close.accepted.connect(self.trigger_save_changes)
        self.parent.btn_dialog_close.rejected.connect(self.trigger_discard_changed)
        self.parent.lst_environments.itemChanged.connect(
            self.trigger_current_item_changed
        )
        self.parent.lst_environments.itemSelectionChanged.connect(
            self.trigger_another_item_selected
        )

    def trigger_another_item_selected(self):
        if self.loading_environments:
            return

        currently_selected_environment = self.parent.currently_selected_item()
        print("===> Environment Selected: {}".format(currently_selected_environment))

    def trigger_current_item_changed(self, list_item):
        print("===> Item Changed: {}".format(list_item))

    def trigger_add_environment(self):
        random_environment_name = random_environment()
        self.parent.add_new_environment_widget(random_environment_name)

    def trigger_remove_environment(self):
        self.parent.remove_selected_environment_widget()

    def trigger_discard_changed(self):
        self.parent.close()

    def trigger_save_changes(self):
        environments = self.parent.environments()
        self.world.environment_store.upsert_environments(environments)
        self.parent.close()

    def show_dialog(self):
        self.loading_environments = True
        environments = self.world.environment_store.get_environments()
        for env in environments:
            self.parent.add_new_environment_widget(env.name)
        self.loading_environments = False
        self.parent.show()
