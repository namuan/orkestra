from app.sections.httpstep.http_step_view import HttpStepView
from app.sections.sqlstep.sql_step_view import SqlStepView
from . import get_main_window


def show_window(qtbot, clear_steps=True):
    window = get_main_window()
    qtbot.addWidget(window)
    if clear_steps:
        window.world.step_store.delete_all_steps()

    return window


def add_step(window, step_name):
    window.default_page_controller.trigger_add_step_command(step_name)


def test_switching_steps(qtbot):
    # given
    window = show_window(qtbot)
    add_step(window, "HTTP")
    add_step(window, "SQL")

    first_idx = window.lst_steps.model().index(0, 0)
    second_idx = window.lst_steps.model().index(1, 0)

    # when
    window.lst_steps.setCurrentIndex(first_idx)

    # then
    assert type(window.stackedWidget.currentWidget()) == HttpStepView, \
        "Should switch to HttpStepWidget"

    # and
    window.lst_steps.setCurrentIndex(second_idx)

    # # then
    assert type(window.stackedWidget.currentWidget()) == SqlStepView, \
        "Should switch to SqlStepWidget"


def test_default_step_if_all_steps_are_deleted(qtbot):
    # given
    window = show_window(qtbot)
    add_step(window, "HTTP")

    # when (delete selected step)
    window.step_list_view.on_delete_selected_item()

    # then (should display default stack page)
    assert window.stackedWidget.currentIndex() == 0
