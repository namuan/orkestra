from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialogButtonBox

from . import get_main_window

NO_OF_ENVIRONMENTS = 5


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

    # and
    env_list_combo = window.environment_list_view.get_environment_list_combo()
    assert env_list_combo.count() == NO_OF_ENVIRONMENTS, \
        "Environments not loaded in toolbar on fresh re-start"


def test_discard_envs_changes_on_cancel(qtbot):
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
    cancel_button = window.environment_view.btn_dialog_close.button(QDialogButtonBox.Cancel)
    qtbot.mouseClick(cancel_button, QtCore.Qt.LeftButton)

    # then
    environments = window.world.environment_store.get_environments()
    assert len(environments) == 0


def test_discard_envs_changes_on_esc(qtbot):
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
    qtbot.keyClick(window.environment_view.lst_environments, Qt.Key_Escape)

    # then
    environments = window.world.environment_store.get_environments()
    assert len(environments) == 0
