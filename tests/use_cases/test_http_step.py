from PyQt6 import QtCore
from PyQt6.QtCore import QItemSelectionModel

from app.core.dynamic_string import DynamicStringData
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
    window.step_list_view.lst_steps.selectionModel().select(selected_index, QItemSelectionModel.SelectionFlag.Deselect)


def select_step(window, position):
    selected_item = window.step_list_view.model.item(position)
    window.step_list_view.lst_steps.selectionModel().select(selected_item.index(), QItemSelectionModel.SelectionFlag.Select)


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


def get_headers_list(window):
    return window.http_step_view.lst_http_headers


def get_query_params_list(window):
    return window.http_step_view.lst_http_query_params


def add_key_value_param(key_value_list_widget, var_name="Test Var Name", var_value="Test Var Value", position=0):
    key_value_list_widget.setup_new_key_value_widget(var_name, DynamicStringData(value=var_value), position)


def build_http_get_request(window):
    window.http_step_view.txt_http_step_title.setText("A New Request")
    window.http_step_view.txt_http_step_description.setPlainText("New Request Description")
    # headers
    add_key_value_param(get_headers_list(window), "Content-Type", "application/json")
    # query params
    add_key_value_param(get_query_params_list(window), "Client", "Orkestra")


def test_send_http_get_request(qtbot):
    # given (new window)
    window = show_window(qtbot)

    # and: add a new HTTP step
    add_step(window, "HTTP")

    # and: populate http request
    build_http_get_request(window)

    # when: press Send
    qtbot.mouseClick(window.http_step_view.btn_send_request, QtCore.Qt.MouseButton.LeftButton)

    # interact(qtbot)

    # then: wait for response
    # and: check raw request field
    assert window.http_step_view.txt_http_raw_request.toPlainText() != ''
    # and: check raw response field
    assert window.http_step_view.txt_http_raw_response.toPlainText() != ''
    # and: check formatted response field
    assert window.http_step_view.txt_http_formatted_response.toPlainText() != ''


def test_send_http_post_request(qtbot):
    # Send request to test post data
    pass


def test_send_http_form_request(qtbot):
    # Send request to test form params
    pass


def test_send_http_error_request(qtbot):
    # Send request to simulate 4xx/5xx errors
    pass
