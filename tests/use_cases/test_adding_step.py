from . import get_main_window


def test_add_new_steps(qtbot):
    # given
    window = get_main_window()
    qtbot.addWidget(window)

    # when
    window.toolbar_controller.trigger_add_step_command("HTTP")
    window.toolbar_controller.trigger_add_step_command("SQL")

    # then
    assert window.lst_steps.model().rowCount() == 2, \
        "Unable to add steps using the toolbar button"


def test_save_new_steps_in_database(qtbot):
    # given
    window = get_main_window()
    qtbot.addWidget(window)
    window.world.step_store.clear_all_steps()

    # when
    window.toolbar_controller.trigger_add_step_command("HTTP")
    window.toolbar_controller.trigger_add_step_command("SQL")

    # then
    steps = window.world.step_store.get_steps()
    assert len(steps) == 2, "Unable to save steps in database"
