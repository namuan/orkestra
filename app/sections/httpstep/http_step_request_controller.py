from app.core.step_types import StepType
from app.sections.step.step_store import StepEntity


class HttpStepRequestController:
    def __init__(self, parent, world):
        self.parent = parent
        self.world = world
        self.current_step_id = None

        # domain events
        self.world.data.events.step_added.connect(self.on_step_added)
        self.world.data.events.step_selection_changed.connect(
            self.on_step_selection_changed
        )

        # world events
        self.world.events.worker_started.connect(self.on_worker_started)
        self.world.events.worker_stopped.connect(self.on_worker_stopped)

    def on_worker_stopped(self):
        self.parent.enable_send_button()

    def on_worker_started(self):
        self.parent.disable_send_button()

    def on_step_added(self, step_id):
        step_entity: StepEntity = self.world.step_store.get_step(step_id)
        if step_entity.step_type == StepType.HTTP:
            self.parent.object_to_form(step_entity)

    def on_step_selection_changed(self, step_id):
        self.current_step_id = step_id

    def trigger_run_http_step(self, run_step_command):
        step_entity: StepEntity = self.world.step_store.get_step(run_step_command.step_id)
        step_data = self.parent.form_to_object()
        step_entity.step_data = step_data
        self.world.step_store.update_steps([step_entity])
        run_step_command.step_entity = step_entity
        self.world.worker_pool.schedule(run_step_command)
