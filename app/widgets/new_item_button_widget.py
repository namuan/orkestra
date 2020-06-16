from PyQt5 import QtWidgets

from app.generated.NewItemWidget_ui import Ui_NewItemWidget


class NewItemButtonWidget(QtWidgets.QWidget, Ui_NewItemWidget):
    def __init__(self, parent=None, on_btn_new_item_pressed=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setLayout(self.horizontalLayout)
        self.btn_new_item.pressed.connect(on_btn_new_item_pressed)
