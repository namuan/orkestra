from app.widgets.http_step_widget import HttpStepWidget
from app.widgets.sql_step_widget import SqlStepWidget
from . import get_main_window


def show_window(qtbot, clear_steps=True):
    window = get_main_window()
    qtbot.addWidget(window)
    if clear_steps:
        window.world.step_store.delete_all_steps()

    return window


def test_switching_steps(qtbot):
    # given
    window = show_window(qtbot)
    window.toolbar_controller.trigger_add_step_command("HTTP")
    window.toolbar_controller.trigger_add_step_command("SQL")

    first_idx = window.lst_steps.model().index(0, 0)
    second_idx = window.lst_steps.model().index(1, 0)

    # when
    window.lst_steps.setCurrentIndex(first_idx)

    # then
    assert type(window.stackedWidget.currentWidget()) == HttpStepWidget, \
        "Should switch to HttpStepWidget"

    # and
    window.lst_steps.setCurrentIndex(second_idx)

    # # then
    assert type(window.stackedWidget.currentWidget()) == SqlStepWidget, \
        "Should switch to SqlStepWidget"


def test_default_step_if_all_steps_are_deleted(qtbot):
    pass
