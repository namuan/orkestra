from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialogButtonBox

from . import get_main_window

NO_OF_ENVIRONMENTS = 5


def test_saving_envs(qtbot):
    # given
    window = get_main_window()
    qtbot.addWidget(window)
    window.environment_view.show_dialog()

    # and (adding a few environments)
    for i in range(NO_OF_ENVIRONMENTS):
        qtbot.mouseClick(window.environment_view.btn_add_environment, QtCore.Qt.LeftButton)

    # when
    ok_button = window.environment_view.btn_dialog_close.button(QDialogButtonBox.Ok)
    qtbot.mouseClick(ok_button, QtCore.Qt.LeftButton)

    # then
    environments = window.world.environment_store.get_environments()
    assert len(environments) == NO_OF_ENVIRONMENTS, "Environments not being saved in database"

    # and (re-opening the dialog box after close)
    window.environment_view.show_dialog()

    # then
    assert window.environment_view.lst_environments.count() == NO_OF_ENVIRONMENTS, \
        "Seems like the dialog box is reloading environments"


def test_loading_envs(qtbot):
    # given
    window = get_main_window()
    qtbot.addWidget(window)

    # when
    window.environment_view.show_dialog()

    # then
    assert window.environment_view.lst_environments.count() == NO_OF_ENVIRONMENTS, \
        "Environments not being loaded from database on a fresh re-start"
