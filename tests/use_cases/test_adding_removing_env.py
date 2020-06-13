from PyQt5 import QtCore

from . import get_main_window


def test_adding_removing_env(qtbot):
    # given
    window = get_main_window()
    qtbot.addWidget(window)
    window.world.environment_store.clear_environments()

    window.environment_view.show_dialog()
    no_of_environments = 5

    # when
    for i in range(no_of_environments):
        qtbot.mouseClick(window.environment_view.btn_add_environment, QtCore.Qt.LeftButton)

    # then
    assert window.environment_view.lst_environments.count() == no_of_environments

    # remove
    for i in range(no_of_environments):
        qtbot.mouseClick(window.environment_view.btn_remove_environment, QtCore.Qt.LeftButton)

    # then
    assert window.environment_view.lst_environments.count() == 0
