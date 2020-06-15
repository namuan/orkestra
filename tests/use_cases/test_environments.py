from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialogButtonBox

from . import get_main_window, close_application

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


def test_adding_removing_env(qtbot):
    # given
    window = show_window(qtbot)

    # when
    add_environments(qtbot, window, NO_OF_ENVIRONMENTS)

    # then
    assert window.environment_view.lst_environments.count() == NO_OF_ENVIRONMENTS

    # remove
    remove_environments(qtbot, window, NO_OF_ENVIRONMENTS)

    # then
    assert window.environment_view.lst_environments.count() == 0


def test_renaming_environment(qtbot):
    # given a window
    window = show_window(qtbot)

    # add a few environments
    add_environments(qtbot, window, NO_OF_ENVIRONMENTS)

    # select an environment from list
    window.environment_view.lst_environments.setCurrentRow(2)
    currently_selected = window.environment_view.lst_environments.currentItem()

    # edit list item
    new_environment_name = "Development"
    currently_selected.setText(new_environment_name)

    # save and close application
    close_and_save_environments(qtbot, window)

    # get environments from controller
    environments = [e.name for e in window.environment_list_view.world.environment_store.get_environments()]
    assert new_environment_name in environments


def test_saving_envs(qtbot):
    # given
    window = show_window(qtbot)

    # and (adding a few environments)
    add_environments(qtbot, window, NO_OF_ENVIRONMENTS)

    # when
    close_and_save_environments(qtbot, window)

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
    window = show_window(qtbot)

    # and (adding a few environments)
    add_environments(qtbot, window, NO_OF_ENVIRONMENTS)

    # and (save)
    close_and_save_environments(qtbot, window)

    # and (close app)
    close_application(window)

    # when
    window = show_window(qtbot, clear_environments=False)

    # then
    env_list_combo = get_toolbar_environments_combo(window)
    assert env_list_combo.count() == NO_OF_ENVIRONMENTS, \
        "Environments not loaded in toolbar on fresh re-start"

    # and
    assert window.environment_view.lst_environments.count() == NO_OF_ENVIRONMENTS, \
        "Environments not being loaded from database on a fresh re-start"


def test_discard_envs_changes_on_cancel(qtbot):
    # given
    window = show_window(qtbot)

    # when
    add_environments(qtbot, window, NO_OF_ENVIRONMENTS)

    # then
    close_and_discard_changes(qtbot, window)

    # then
    environments = window.world.environment_store.get_environments()
    assert len(environments) == 0


def test_discard_envs_changes_on_esc(qtbot):
    # given
    window = show_window(qtbot)

    # when
    add_environments(qtbot, window, NO_OF_ENVIRONMENTS)

    # then
    qtbot.keyClick(window.environment_view.lst_environments, Qt.Key_Escape)

    # then
    environments = window.world.environment_store.get_environments()
    assert len(environments) == 0


def test_refresh_toolbar_after_adding_deleting_envs(qtbot):
    # given
    window = show_window(qtbot)

    # and (adding a few environments)
    add_environments(qtbot, window, NO_OF_ENVIRONMENTS)

    # when (click ok to save environments)
    close_and_save_environments(qtbot, window)

    # then (check toolbar environments)
    assert get_toolbar_environments_combo(window).count() == NO_OF_ENVIRONMENTS, \
        "Environments not loaded in toolbar on after Environments Dialog close"

    # and (re-opening the dialog box after close)
    window.environment_view.show_dialog()

    # and (delete 3 and add 1 environment(s))
    remove_environments(qtbot, window, NO_OF_ENVIRONMENTS_TO_DELETE)

    add_environments(qtbot, window, NO_OF_ENVIRONMENTS_TO_RE_ADD)

    # and (click ok to save environments)
    close_and_save_environments(qtbot, window)

    # then (check toolbar environments)
    remaining_environments = NO_OF_ENVIRONMENTS - NO_OF_ENVIRONMENTS_TO_DELETE + NO_OF_ENVIRONMENTS_TO_RE_ADD
    assert get_toolbar_environments_combo(window).count() == remaining_environments, \
        "Environments not loaded in toolbar on (deleting/re-adding) after Environments Dialog close"


def test_update_currently_selected_environment(qtbot):
    # given (a window with few environments)
    window = show_window(qtbot)

    # and
    add_environments(qtbot, window, NO_OF_ENVIRONMENTS)

    # and
    close_and_save_environments(qtbot, window)

    # when (a new environment is selected from toolbar)
    toolbar_environments = get_toolbar_environments_combo(window)
    toolbar_environments.setCurrentIndex(3)
    selected_environment = toolbar_environments.currentText()

    # and application is closed
    window.toolbar_controller.trigger_quit_application()

    # and window is re-opened
    window = show_window(qtbot)

    # then the selected environment should be same as before
    toolbar_environments = get_toolbar_environments_combo(window)
    selected_environment_after_restart = toolbar_environments.currentText()
    assert selected_environment == selected_environment_after_restart
