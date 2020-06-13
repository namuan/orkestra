class StepListController:
    def __init__(self, parent_view, world):
        self.parent_view = parent_view
        self.world = world

        # domain events
        self.world.data.events.step_added.connect(self.on_step_added)

    def on_step_added(self, step_id):
        step = self.world.step_store.get_step(step_id)
        self.parent_view.add_step_widget(step)

    def trigger_step_selected(self, selected_step_id):
        self.world.app_state_store.update_selected_step(selected_step_id)