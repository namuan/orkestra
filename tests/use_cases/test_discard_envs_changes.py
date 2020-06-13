from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialogButtonBox

from . import get_main_window


def test_discard_envs_changes_on_cancel(qtbot):
    # given
    window = get_main_window()
    qtbot.addWidget(window)
    window.environment_view.show_dialog()
    no_of_environments = 5
    window.world.environment_store.clear_environments()

    # when
    for i in range(no_of_environments):
        qtbot.mouseClick(window.environment_view.btn_add_environment, QtCore.Qt.LeftButton)

    # then
    cancel_button = window.environment_view.btn_dialog_close.button(QDialogButtonBox.Cancel)
    qtbot.mouseClick(cancel_button, QtCore.Qt.LeftButton)

    # then
    environments = window.world.environment_store.get_environments()
    assert len(environments) == 0


def test_discard_envs_changes_on_esc(qtbot):
    # given
    window = get_main_window()
    qtbot.addWidget(window)
    window.environment_view.show_dialog()
    no_of_environments = 5
    window.world.environment_store.clear_environments()

    # when
    for i in range(no_of_environments):
        qtbot.mouseClick(window.environment_view.btn_add_environment, QtCore.Qt.LeftButton)

    # then
    qtbot.keyClick(window.environment_view.lst_environments, Qt.Key_Escape)

    # then
    environments = window.world.environment_store.get_environments()
    assert len(environments) == 0
