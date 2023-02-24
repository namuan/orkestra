from PyQt6 import QtWidgets

from app.core.dynamic_string import DynamicStringData
from app.generated.KeyValueWidget_ui import Ui_KeyValueWidget


class KeyValueWidget(QtWidgets.QWidget, Ui_KeyValueWidget):
    def __init__(self, parent=None, parent_widget_item=None, on_remove_callback=None):
        super(KeyValueWidget, self).__init__(parent)
        self.setupUi(self)
        self.k = ""
        self.v = DynamicStringData()
        self.setLayout(self.horizontalLayout)
        self.btn_remove_item.pressed.connect(
            lambda: on_remove_callback(parent_widget_item)
        )

    def set_data(self, name, v: DynamicStringData):
        self.k = name
        self.v = v

        self.txt_item_name.setText(self.k)
        self.txt_item_value.setText(self.v.value)
        self.chk_item_enabled.setChecked(v.is_enabled)

    def get_data(self):
        self.k = self.txt_item_name.text().strip()
        self.v.value = self.txt_item_value.text().strip()
        self.v.is_enabled = self.chk_item_enabled.isChecked()
        return self.k, self.v
