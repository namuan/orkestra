from PyQt5 import QtCore

from app.widgets.http_step_widget import HttpStepWidget
from app.widgets.sql_step_widget import SqlStepWidget
from . import get_main_window


def show_window(qtbot, clear_steps=True):
    window = get_main_window()
    qtbot.addWidget(window)
    if clear_steps:
        window.world.step_store.delete_all_steps()

    return window


def test_adding_http_widget_from_default_page(qtbot):
    # given
    window = show_window(qtbot)

    # when
    qtbot.mouseClick(window.btn_new_http_request, QtCore.Qt.LeftButton)

    # then
    assert type(window.stackedWidget.currentWidget()) == HttpStepWidget, \
        "Should switch to HttpStepWidget"


def test_adding_sql_widget_from_default_page(qtbot):
    # given
    window = show_window(qtbot)

    # when
    qtbot.mouseClick(window.btn_new_sql_request, QtCore.Qt.LeftButton)

    # then
    assert type(window.stackedWidget.currentWidget()) == SqlStepWidget, \
        "Should switch to SqlStepWidget"
