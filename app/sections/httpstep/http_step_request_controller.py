class HttpStepRequestController:
    def __init__(self, parent, world):
        self.parent = parent
        self.world = world

        # domain events
        self.world.data.events.step_added.connect(self.on_step_added)

    def on_step_added(self, step_id):
        step_entity = self.world.step_store.get_step(step_id)
        self.parent.object_to_form(step_entity)
