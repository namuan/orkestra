class EnvironmentListController:
    def __init__(self, parent, world):
        self.parent = parent
        self.world = world

        # app start event
        self.world.data.events.app_started.connect(self.on_repopulate_environments)

        # domain events
        self.world.data.events.environments_changed.connect(self.on_repopulate_environments)

    def on_repopulate_environments(self):
        environments = self.world.environment_store.get_environments()
        self.parent.populate_environments(environments)
