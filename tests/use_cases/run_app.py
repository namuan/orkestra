from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialogButtonBox, QListWidgetItem

from app.core.faker_config import fake
from . import get_main_window, interact


def show_window(qtbot, clear_state=True):
    window = get_main_window()
    qtbot.addWidget(window)
    if clear_state:
        window.world.step_store.delete_all_steps()
        window.world.environment_store.clear_environments()

    return window


def add_environments(qtbot, window, number):
    for i in range(number):
        qtbot.mouseClick(window.environment_view.btn_add_environment, QtCore.Qt.LeftButton)


def close_and_save_environments(qtbot, window):
    ok_button = window.environment_view.btn_dialog_close.button(QDialogButtonBox.Ok)
    qtbot.mouseClick(ok_button, QtCore.Qt.LeftButton)


def add_step(window, step_name):
    window.default_page_controller.trigger_add_step_command(step_name)


def get_key_value_list(window):
    environments_variables_list_widget = window.environment_view.lst_environment_variables
    return environments_variables_list_widget.key_value_item_list


def get_key_value_widget(window, position=0):
    key_value_list = get_key_value_list(window)
    item: QListWidgetItem = key_value_list.item(position)
    return key_value_list.itemWidget(item)


def add_environment_variable(qtbot, window, var_name="Test Var Name", var_value="Test Var Value", position=0):
    environments_variables_list_widget = window.environment_view.lst_environment_variables
    environments_variables_list_widget.on_new_item_pressed()
    key_value_widget = get_key_value_widget(window, position)
    qtbot.keyClicks(key_value_widget.txt_item_name, var_name)
    qtbot.keyClicks(key_value_widget.txt_item_value, var_value)


def select_environment(window, position):
    window.environment_view.lst_environments.setCurrentRow(position)
    return window.environment_view.lst_environments.currentItem().text()


def set_environment_variables(qtbot, window, selected_env):
    selected_environment_name = select_environment(window, position=selected_env.get('position'))
    for i in range(len(selected_env.get('data'))):
        add_environment_variable(qtbot, window, *selected_env.get('data')[i], position=i)
    return selected_environment_name


def test_app_with_prepopulated_data(qtbot):
    # given (a new window)
    window = show_window(qtbot)

    # add some environments
    window.environment_view.show_dialog()
    add_environments(qtbot, window, 5)
    close_and_save_environments(qtbot, window)

    # add some environment variables
    selected_env = dict(
        position=2,
        data=[(fake.domain_word(), fake.first_name()) for _ in range(5)]
    )
    set_environment_variables(qtbot, window, selected_env)

    # add some steps
    for i in range(10):
        add_step(window, "HTTP")
        add_step(window, "SQL")

    interact(qtbot)
