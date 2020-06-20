from . import get_main_window


def show_window(qtbot, clear_steps=True):
    window = get_main_window()
    qtbot.addWidget(window)
    if clear_steps:
        window.world.step_store.clear_all_steps()

    return window


def test_add_new_steps(qtbot):
    # given
    window = show_window(qtbot)

    # when
    window.toolbar_controller.trigger_add_step_command("HTTP")
    window.toolbar_controller.trigger_add_step_command("SQL")

    # then
    assert window.lst_steps.model().rowCount() == 2, \
        "Unable to add steps using the toolbar button"


def test_save_new_steps_in_database(qtbot):
    # given
    window = show_window(qtbot)

    # when
    window.toolbar_controller.trigger_add_step_command("HTTP")
    window.toolbar_controller.trigger_add_step_command("SQL")

    # then
    steps = window.world.step_store.get_steps()
    assert len(steps) == 2, "Unable to save steps in database"


def test_load_steps_from_database(qtbot):
    # given
    window = show_window(qtbot)

    # and (add few steps)
    window.toolbar_controller.trigger_add_step_command("HTTP")
    window.toolbar_controller.trigger_add_step_command("SQL")

    # when (quit application)
    window.toolbar_controller.trigger_quit_application()

    # and (re-start)
    window = show_window(qtbot, clear_steps=False)

    # then
    assert window.lst_steps.model().rowCount() == 2, \
        "Unable to add steps after re-start"
