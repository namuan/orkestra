class StepListController:
    def __init__(self, parent, world):
        self.parent = parent
        self.world = world

        # app start event
        self.world.data.events.app_started.connect(self.on_repopulate_steps)

        # domain events
        self.world.data.events.step_added.connect(self.on_step_added)
        self.world.data.events.steps_deleted.connect(self.on_repopulate_steps)

    def on_repopulate_steps(self):
        steps = self.world.step_store.get_steps()
        self.parent.clear_steps()
        self.parent.update_steps(steps)

    def on_step_added(self, step_id):
        step = self.world.step_store.get_step(step_id)
        self.parent.add_step_widget(step)

    def trigger_step_selected(self, selected_step_id):
        self.world.app_state_store.update_selected_step(selected_step_id)
