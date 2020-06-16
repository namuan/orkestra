from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QListWidgetItem

from app.core.dynamic_string import DynamicStringData
from app.generated.KeyValueListWidget_ui import Ui_KeyValueListWidget
from app.widgets.key_value_list_controller import KeyValueListController
from app.widgets.key_value_widget import KeyValueWidget
from app.widgets.new_item_button_widget import NewItemButtonWidget


class KeyValueListWidget(QtWidgets.QWidget, Ui_KeyValueListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.controller = KeyValueListController(self)
        self.setup_new_item_widget()

    def setup_new_item_widget(self):
        item = QListWidgetItem()
        new_item_widget = NewItemButtonWidget(
            self.key_value_item_list, on_btn_new_item_pressed=self.on_new_item_pressed
        )
        item.setSizeHint(new_item_widget.sizeHint())

        self.key_value_item_list.addItem(item)
        self.key_value_item_list.setItemWidget(item, new_item_widget)

    def on_new_item_pressed(self):
        total_items = self.key_value_item_list.count()
        self.setup_new_key_value_widget("", DynamicStringData(), total_items - 1)

    def setup_new_key_value_widget(self, key, value, item_position):
        item = QListWidgetItem()
        kv_widget = KeyValueWidget(
            self.key_value_item_list, item, self.remove_key_value_widget
        )
        kv_widget.set_data(key, value)
        item.setSizeHint(kv_widget.sizeHint())
        self.key_value_item_list.insertItem(item_position, item)
        self.key_value_item_list.setItemWidget(item, kv_widget)

    def remove_key_value_widget(self, widget_item):
        self.key_value_item_list.takeItem(self.key_value_item_list.row(widget_item))
