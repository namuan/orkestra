from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QListView

from app.controllers import StepListController
from app.data.step import StepEntity


class StepListView:
    def __init__(self, main_window):
        self.main_window = main_window
        self.lst_steps: QListView = self.main_window.lst_steps
        self.controller = StepListController(self, self.main_window.world)

        # setup model
        self.model = QStandardItemModel()
        self.lst_steps.setModel(self.model)

    def add_step_widget(self, step: StepEntity):
        print("Adding a new widget for {}".format(step))
        step_item = QStandardItem("({}) {}".format(step.step_type.value, step.title))
        self.model.appendRow(step_item)
