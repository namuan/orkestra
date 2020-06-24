import logging

from PyQt5.QtCore import Qt, QModelIndex, QVariant
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMenu, QAction

from app.core.constants import STEP_LIST_OBJECT_ROLE, STEP_LIST_ID_ROLE
from app.widgets.steps_list_widget import StepItemDelegate, CustomStepsListView
from .step_list_controller import StepListController
from .step_store import StepEntity


class StepListView:
    def __init__(self, main_window):
        self.main_window = main_window
        self.lst_steps: CustomStepsListView = self.main_window.lst_steps
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
        self.lst_steps.dropEventSignal.connect(self.on_drop_event)

    def on_drop_event(self, model_index: QModelIndex):
        selected_model_indexes = self.lst_steps.selectedIndexes()
        self.delete_steps_by_indexes(selected_model_indexes, delete_from_db=False)

        def step_with_order(order):
            step_entity = self.model.item(order).data(STEP_LIST_OBJECT_ROLE)
            step_entity.order = order
            return step_entity

        steps = [step_with_order(n) for n in range(self.model.rowCount())]
        self.controller.update_multiple_steps(steps)

    def get_step_entity_at_index(self, model_index):
        return model_index.data(STEP_LIST_OBJECT_ROLE)

    def select_step_at_index(self, model_index):
        self.lst_steps.setCurrentIndex(model_index)

    def indexes_for_selected_rows(self):
        return self.lst_steps.selectedIndexes()

    def delete_steps_by_indexes(self, model_indexes, delete_from_db=True):
        for items in reversed(sorted(model_indexes)):
            if delete_from_db:
                step_entity: StepEntity = self.get_step_entity_at_index(items)
                self.controller.delete_step(step_entity)
            self.model.takeRow(items.row())

    def on_delete_selected_item(self):
        selected_model_indexes = self.indexes_for_selected_rows()
        if not selected_model_indexes:
            return

        self.delete_steps_by_indexes(selected_model_indexes)

        before_first_row_to_delete = selected_model_indexes[0].row() - 1
        if before_first_row_to_delete >= 0:
            previous_item: QStandardItem = self.model.item(before_first_row_to_delete)
            self.select_step_at_index(previous_item.index())

    def on_display_context_menu(self, position):
        index: QModelIndex = self.lst_steps.indexAt(position)
        if not index.isValid():
            return

        global_position = self.lst_steps.viewport().mapToGlobal(position)
        self.menu.exec_(global_position)

    def clear_steps(self):
        self.model.clear()

    def update_steps(self, steps):
        for step in steps:
            self.add_step_widget(step, select_item=False)

    def select_step_at(self, position):
        first_item: QStandardItem = self.model.item(position)
        self.lst_steps.setCurrentIndex(first_item.index())

    def add_step_widget(self, step: StepEntity, select_item=True):
        logging.info("Adding a new widget for {}".format(step))
        step_item = QStandardItem("({}) {}".format(step.step_type.value, step.title))
        step_item.setData(step, STEP_LIST_OBJECT_ROLE)
        step_item.setData(QVariant(step.id), STEP_LIST_ID_ROLE)
        step_item.setDragEnabled(True)
        step_item.setDropEnabled(False)
        self.model.appendRow(step_item)

        if select_item:
            index = self.model.indexFromItem(step_item)
            self.lst_steps.setCurrentIndex(index)

    def on_step_selected(self, current: QModelIndex):
        if not current:
            return

        selected_step_id = current.data(STEP_LIST_ID_ROLE)
        self.controller.trigger_step_selected(selected_step_id)
