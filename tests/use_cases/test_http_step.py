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


def test_add_new_http_steps(qtbot):
    # given
    window = show_window(qtbot)

    # when
    add_step(window, "HTTP")

    # then
    assert window.http_step_view
    assert window.lst_steps.model().rowCount() == 1, \
        "Unable to add steps using the toolbar button"
    assert window.http_step_view.cmb_http_method.currentText() == "GET"
    assert window.http_step_view.txt_http_url.text() == "https://httpbin.org/get"
