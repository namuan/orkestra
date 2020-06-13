from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialogButtonBox

from . import get_main_window


def test_saving_envs(qtbot):
    # given
    window = get_main_window()
    qtbot.addWidget(window)
    window.environment_view.show_dialog()
    no_of_environments = 5

    # when
    for i in range(no_of_environments):
        qtbot.mouseClick(window.environment_view.btn_add_environment, QtCore.Qt.LeftButton)

    # then
    ok_button = window.environment_view.btn_dialog_close.button(QDialogButtonBox.Ok)
    qtbot.mouseClick(ok_button, QtCore.Qt.LeftButton)

    # then
    environments = window.world.environment_store.get_environments()
    assert len(environments) == 5
