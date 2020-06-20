import logging
from functools import partial

from app.commands.add_step_command import AddStepCommand
from app.core.step_types import StepType


class DefaultPageController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.world = main_window.world

        # ui events
        self.main_window.btn_new_http_request.pressed.connect(
            partial(self.trigger_add_step_command, "HTTP")
        )
        self.main_window.btn_new_sql_request.pressed.connect(
            partial(self.trigger_add_step_command, "SQL")
        )

    def trigger_add_step_command(self, step_name):
        add_step_command = AddStepCommand(step_type=StepType[step_name])
        logging.info("Adding new step: {}".format(add_step_command))
        self.world.step_store.add_step(add_step_command)
