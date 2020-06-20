from . import get_main_window


def show_window(qtbot, clear_steps=True):
    window = get_main_window()
    qtbot.addWidget(window)
    if clear_steps:
        window.world.step_store.delete_all_steps()

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


def test_delete_step(qtbot):
    # given
    window = show_window(qtbot)

    # and (add few steps)
    window.toolbar_controller.trigger_add_step_command("HTTP")
    window.toolbar_controller.trigger_add_step_command("SQL")

    # and (select one step)
    selected_item_index = window.step_list_view.model.item(1)
    window.step_list_view.lst_steps.setCurrentIndex(selected_item_index.index())

    # when (delete by triggering context menu action
    window.step_list_view.on_delete_selected_item()

    # then (it should be removed from list view)
    assert window.lst_steps.model().rowCount() == 1, \
        "Unable to delete step"

    # and (it should be removed from database)
    steps_in_db = window.world.step_store.get_steps()
    assert len(steps_in_db) == 1
