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
        steps = self.world.step_store.get_sorted_steps()
        self.parent.clear_steps()
        self.parent.update_steps(steps)
        if len(steps) > 0:
            self.parent.select_step_at(position=0)

    def on_step_added(self, step_id):
        step = self.world.step_store.get_step(step_id)
        self.parent.add_step_widget(step)

    def trigger_step_selected(self, selected_step_id):
        self.world.app_state_store.update_selected_step(selected_step_id)

    def delete_step(self, step_entity):
        self.world.step_store.delete_single_step(step_entity.id)

    def update_multiple_steps(self, steps):
        self.world.step_store.update_multiple_steps(steps)
