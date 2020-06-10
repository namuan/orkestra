import logging

from PyQt5.QtCore import QModelIndex, QVariant
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QListView

from app.controllers import StepListController
from app.core.constants import STEP_LIST_OBJECT_ROLE, STEP_LIST_ID_ROLE
from app.data.step import StepEntity


class StepListView:
    def __init__(self, main_window):
        self.main_window = main_window
        self.lst_steps: QListView = self.main_window.lst_steps
        self.controller = StepListController(self, self.main_window.world)

        # setup model
        self.model = QStandardItemModel()
        self.lst_steps.setModel(self.model)

        # ui events
        self.lst_steps.selectionModel().currentChanged.connect(self.on_step_selected)

    def add_step_widget(self, step: StepEntity):
        logging.info("Adding a new widget for {}".format(step))
        step_item = QStandardItem("({}) {}".format(step.step_type.value, step.title))
        step_item.setData(step, STEP_LIST_OBJECT_ROLE)
        step_item.setData(QVariant(step.id), STEP_LIST_ID_ROLE)
        self.model.appendRow(step_item)

    def on_step_selected(self, current: QModelIndex):
        if not current:
            return

        selected_step_id = current.data(STEP_LIST_ID_ROLE)
        self.controller.trigger_step_selected(selected_step_id)
