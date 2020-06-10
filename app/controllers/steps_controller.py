import logging

from app.commands.add_step_command import AddStepCommand
from app.core.step_types import StepType


class StepsController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.world = self.main_window.world

    def trigger_add_step_command(self, step_name):
        add_step_command = AddStepCommand(name=step_name, step_type=StepType[step_name])
        logging.info("Adding new step: {}".format(add_step_command))
        self.world.step_store.add_step(add_step_command)
