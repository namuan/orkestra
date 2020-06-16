class EnvironmentListController:
    def __init__(self, parent, world):
        self.parent = parent
        self.world = world

        # app start event
        self.world.data.events.app_started.connect(self.on_repopulate_environments)

        # domain events
        self.world.data.events.environments_changed.connect(
            self.on_repopulate_environments
        )

    def on_repopulate_environments(self):
        selected_environment = self.world.app_state_store.app_state.selected_environment
        environments = self.world.environment_store.get_environments()
        self.parent.populate_environments(environments)
        self.parent.set_toolbar_current_environment(selected_environment)

    def current_environment_changed(self, new_environment):
        self.world.app_state_store.update_selected_environment(new_environment)
