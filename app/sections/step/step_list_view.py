import logging

from PyQt5.QtCore import Qt, QModelIndex, QVariant, QItemSelectionModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QListView, QMenu, QAction

from app.core.constants import STEP_LIST_OBJECT_ROLE, STEP_LIST_ID_ROLE
from app.widgets.steps_list_widget import StepItemDelegate
from .step_list_controller import StepListController
from .step_store import StepEntity


class StepListView:
    def __init__(self, main_window):
        self.main_window = main_window
        self.lst_steps: QListView = self.main_window.lst_steps
        self.controller = StepListController(self, self.main_window.world)

        # menu
        delete_action = QAction("Delete", self.lst_steps)
        delete_action.triggered.connect(self.on_delete_selected_item)

        self.menu = QMenu()
        self.menu.addAction(delete_action)

        # setup model
        self.model = QStandardItemModel()
        self.lst_steps.setModel(self.model)
        self.lst_steps.setItemDelegate(StepItemDelegate())

        # ui events
        self.lst_steps.selectionModel().currentChanged.connect(self.on_step_selected)
        self.lst_steps.setContextMenuPolicy(Qt.CustomContextMenu)
        self.lst_steps.customContextMenuRequested.connect(self.on_display_context_menu)

    def index_at_selected_row(self):
        selected_model: QItemSelectionModel = self.lst_steps.selectionModel()
        if not selected_model.hasSelection():
            return None
        return selected_model.currentIndex()

    def on_delete_selected_item(self):
        selected_model_index: QModelIndex = self.index_at_selected_row()
        if not selected_model_index:
            return

        row_to_remove = selected_model_index.row()
        step_entity: StepEntity = selected_model_index.data(STEP_LIST_OBJECT_ROLE)

        self.controller.delete_step(step_entity)

        self.model.removeRow(row_to_remove)
        previous_row = row_to_remove - 1
        if previous_row >= 0:
            previous_item: QStandardItem = self.model.item(previous_row)
            self.lst_steps.setCurrentIndex(previous_item.index())

    def on_display_context_menu(self, position):
        index: QModelIndex = self.lst_steps.indexAt(position)
        if not index.isValid():
            return

        global_position = self.lst_steps.viewport().mapToGlobal(position)
        self.menu.exec_(global_position)

    def clear_steps(self):
        self.model.clear()

    def update_steps(self, steps):
        for step_id, step in steps.items():
            self.add_step_widget(step, select_item=False)

    def select_step_at(self, position):
        first_item: QStandardItem = self.model.item(position)
        self.lst_steps.setCurrentIndex(first_item.index())

    def add_step_widget(self, step: StepEntity, select_item=True):
        logging.info("Adding a new widget for {}".format(step))
        step_item = QStandardItem("({}) {}".format(step.step_type.value, step.title))
        step_item.setData(step, STEP_LIST_OBJECT_ROLE)
        step_item.setData(QVariant(step.id), STEP_LIST_ID_ROLE)
        self.model.appendRow(step_item)

        if select_item:
            index = self.model.indexFromItem(step_item)
            self.lst_steps.setCurrentIndex(index)

    def on_step_selected(self, current: QModelIndex):
        if not current:
            return

        selected_step_id = current.data(STEP_LIST_ID_ROLE)
        self.controller.trigger_step_selected(selected_step_id)
