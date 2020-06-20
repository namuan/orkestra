from PyQt5.QtCore import QItemSelectionModel

from . import get_main_window


def show_window(qtbot, clear_steps=True):
    window = get_main_window()
    qtbot.addWidget(window)
    if clear_steps:
        window.world.step_store.delete_all_steps()

    return window


def add_step(window, step_name):
    window.default_page_controller.trigger_add_step_command(step_name)


def deselect_current_step(window):
    selected_index = window.step_list_view.lst_steps.currentIndex()
    window.step_list_view.lst_steps.selectionModel().select(selected_index, QItemSelectionModel.Deselect)


def select_step(window, position):
    selected_item = window.step_list_view.model.item(position)
    window.step_list_view.lst_steps.selectionModel().select(selected_item.index(), QItemSelectionModel.Select)


def test_add_new_steps(qtbot):
    # given
    window = show_window(qtbot)

    # when
    add_step(window, "HTTP")
    add_step(window, "SQL")

    # then
    assert window.lst_steps.model().rowCount() == 2, \
        "Unable to add steps using the toolbar button"


def test_save_new_steps_in_database(qtbot):
    # given
    window = show_window(qtbot)

    # when
    add_step(window, "HTTP")
    add_step(window, "SQL")

    # then
    steps = window.world.step_store.get_steps()
    assert len(steps) == 2, "Unable to save steps in database"


def test_load_steps_from_database(qtbot):
    # given
    window = show_window(qtbot)

    # and (add few steps)
    add_step(window, "HTTP")
    add_step(window, "SQL")

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
    add_step(window, "HTTP")
    add_step(window, "SQL")

    # and (select one step)
    select_step(window, 1)

    # when (delete by triggering context menu action
    window.step_list_view.on_delete_selected_item()

    # then (it should be removed from list view)
    assert window.lst_steps.model().rowCount() == 1, \
        "Unable to delete step"

    # and (it should be removed from database)
    steps_in_db = window.world.step_store.get_steps()
    assert len(steps_in_db) == 1


def test_delete_multiple_step(qtbot):
    # given
    window = show_window(qtbot)

    # and (add few steps)
    for i in range(3):
        add_step(window, "HTTP")
        add_step(window, "SQL")

    # and (select multiple step)
    deselect_current_step(window)
    select_step(window, 1)
    select_step(window, 2)
    select_step(window, 4)

    # when (delete by triggering context menu action
    window.step_list_view.on_delete_selected_item()

    # then (it should be removed from database)
    steps_in_db = window.world.step_store.get_steps()
    assert len(steps_in_db) == 3

    # and (it should be removed from list view)
    assert window.lst_steps.model().rowCount() == 3, \
        "Unable to delete multiple step"
