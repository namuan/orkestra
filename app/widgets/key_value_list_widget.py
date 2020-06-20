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

    def items(self):
        item_count = self.key_value_item_list.count()
        return {
            item_key: item_value.value
            for item_key, item_value in [
                self.item_widget(i).get_data() for i in range(item_count - 1)
            ]
        }

    def item_widget(self, position):
        item: QListWidgetItem = self.key_value_item_list.item(position)
        return self.key_value_item_list.itemWidget(item)

    def clear(self):
        self.key_value_item_list.clear()
        self.setup_new_item_widget()

    def update_items(self, data_items):
        for i, (k, v) in enumerate(data_items.items()):
            self.setup_new_key_value_widget(k, DynamicStringData(value=v), i)
