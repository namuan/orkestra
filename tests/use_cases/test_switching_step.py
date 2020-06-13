from app.widgets.http_step_widget import HttpStepWidget
from app.widgets.sql_step_widget import SqlStepWidget
from . import get_main_window


def test_switching_steps(qtbot):
    # given
    window = get_main_window()
    qtbot.addWidget(window)
    window.toolbar_controller.trigger_add_step_command("HTTP")
    window.toolbar_controller.trigger_add_step_command("SQL")

    first_idx = window.lst_steps.model().index(0, 0)
    second_idx = window.lst_steps.model().index(1, 0)

    # when
    window.lst_steps.setCurrentIndex(first_idx)

    # then
    assert HttpStepWidget in [type(t) for t in window.detailsFrame.children()]

    # and
    window.lst_steps.setCurrentIndex(second_idx)

    # then
    assert SqlStepWidget in [type(t) for t in window.detailsFrame.children()]
