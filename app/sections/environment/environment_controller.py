from app.core.random_utils import random_environment


class EnvironmentController:
    def __init__(self, parent, world):
        self.parent = parent
        self.world = world
        self.loading_environments = False
        self.selected_environment = None
        self.environments_cache = {}

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

        previously_selected_environment = self.selected_environment
        self.selected_environment = self.parent.selected_environment_name()
        self.save_variables_in_cache(previously_selected_environment)
        self.parent.clear_variables()
        self.load_variables_from_cache(self.selected_environment)

    def save_variables_in_cache(self, environment):
        environment_variables = self.parent.environment_variables()
        self.environments_cache[environment] = environment_variables

    def load_variables_from_cache(self, environment):
        environment_variables = self.environments_cache[environment]
        self.parent.update_environment_variables(environment_variables)

    def trigger_current_item_changed(self, list_item):
        changed_environment_name = list_item.text()
        self.environments_cache[changed_environment_name] = self.environments_cache.pop(self.selected_environment)
        self.selected_environment = changed_environment_name

    def trigger_add_environment(self):
        random_environment_name = random_environment()
        self.add_new_environment(random_environment_name)

    def add_new_environment(self, environment_name):
        self.environments_cache[environment_name] = {}
        self.parent.add_new_environment_widget(environment_name)

    def trigger_remove_environment(self):
        del self.environments_cache[self.parent.selected_environment_name()]
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
            self.add_new_environment(env.name)

        self.selected_environment = self.parent.selected_environment_name()
        self.loading_environments = False
        self.parent.show()
