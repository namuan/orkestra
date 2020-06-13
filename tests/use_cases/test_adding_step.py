from . import get_main_window


def test_add_new_steps(qtbot):
    # given
    window = get_main_window()
    qtbot.addWidget(window)

    # when
    window.toolbar_controller.trigger_add_step_command("HTTP")
    window.toolbar_controller.trigger_add_step_command("SQL")

    # then
    assert window.lst_steps.model().rowCount() == 2
