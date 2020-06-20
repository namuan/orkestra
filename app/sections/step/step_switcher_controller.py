class StepSwitcherController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.world = main_window.world

        # domain events
        self.world.data.events.step_selection_changed.connect(
            self.on_step_selection_changed
        )

    def on_step_selection_changed(self, selected_step_id):
        step = self.world.step_store.get_step(selected_step_id)
        self.main_window.replace_step(step)
