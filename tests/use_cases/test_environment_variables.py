from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialogButtonBox, QListWidgetItem

from app.core.dynamic_string import DynamicStringData
from app.widgets.key_value_widget import KeyValueWidget
from . import get_main_window

NO_OF_ENVIRONMENTS = 5
NO_OF_ENVIRONMENTS_TO_DELETE = 3
NO_OF_ENVIRONMENTS_TO_RE_ADD = 1


def get_toolbar_environments_combo(window):
    return window.environment_list_view.get_environment_list_combo()


def show_window(qtbot, clear_environments=True):
    window = get_main_window()
    qtbot.addWidget(window)
    if clear_environments:
        window.world.environment_store.clear_environments()

    window.environment_view.show_dialog()
    return window


def add_environments(qtbot, window, number):
    for i in range(number):
        qtbot.mouseClick(window.environment_view.btn_add_environment, QtCore.Qt.LeftButton)


def remove_environments(qtbot, window, number):
    for i in range(number):
        qtbot.mouseClick(window.environment_view.btn_remove_environment, QtCore.Qt.LeftButton)


def close_and_save_environments(qtbot, window):
    ok_button = window.environment_view.btn_dialog_close.button(QDialogButtonBox.Ok)
    qtbot.mouseClick(ok_button, QtCore.Qt.LeftButton)


def close_and_discard_changes(qtbot, window):
    cancel_button = window.environment_view.btn_dialog_close.button(QDialogButtonBox.Cancel)
    qtbot.mouseClick(cancel_button, QtCore.Qt.LeftButton)


def get_key_value_widget(window, position=0) -> KeyValueWidget:
    key_value_list = get_key_value_list(window)
    item: QListWidgetItem = key_value_list.item(position)
    return key_value_list.itemWidget(item)


def get_key_value_list(window):
    environments_variables_list_widget = window.environment_view.lst_environment_data
    return environments_variables_list_widget.key_value_item_list


def add_environment_variable(qtbot, window, var_name="Test Var Name", var_value="Test Var Value"):
    environments_variables_list_widget = window.environment_view.lst_environment_data
    environments_variables_list_widget.on_new_item_pressed()
    key_value_widget: KeyValueWidget = get_key_value_widget(window)
    qtbot.keyClicks(key_value_widget.txt_item_name, var_name)
    qtbot.keyClicks(key_value_widget.txt_item_value, var_value)


def test_adding_environment_variables(qtbot):
    # given
    window = show_window(qtbot)
    add_environments(qtbot, window, NO_OF_ENVIRONMENTS)

    # when (add a new key/value row)
    var_name = "Test Data"
    var_value = "Test Data Value"
    add_environment_variable(qtbot, window, var_name, var_value)

    # then
    actual_var_key, actual_var_value = get_key_value_widget(window).get_data()
    assert actual_var_key == var_name
    assert actual_var_value == DynamicStringData(value=var_value, is_enabled=True)


def test_delete_environment_variables_row(qtbot):
    #  given (a new environment row)
    window = show_window(qtbot)
    add_environments(qtbot, window, NO_OF_ENVIRONMENTS)

    # and (add a new key/value variable row)
    add_environment_variable(qtbot, window)

    # when (delete key is pressed)
    key_value_widget = get_key_value_widget(window)
    qtbot.mouseClick(key_value_widget.btn_remove_item, QtCore.Qt.LeftButton)

    # then number of items in list should be 1
    assert get_key_value_list(window).count() == 1
