from app.core.step_types import StepType
from app.widgets.http_step_widget import HttpStepWidget
from app.widgets.sql_step_widget import SqlStepWidget


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
        if step.step_type == StepType.HTTP:
            step_widget = HttpStepWidget(self.main_window.detailsFrame)
        elif step.step_type == StepType.SQL:
            step_widget = SqlStepWidget(self.main_window.detailsFrame)

        self.main_window.replace_widget(step_widget)
