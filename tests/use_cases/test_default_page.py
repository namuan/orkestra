from PyQt5 import QtCore

from app.sections.httpstep.http_step_view import HttpStepView
from app.sections.sqlstep.sql_step_view import SqlStepView
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
    assert type(window.stackedWidget.currentWidget()) == HttpStepView, \
        "Should switch to HttpStepWidget"


def test_adding_sql_widget_from_default_page(qtbot):
    # given
    window = show_window(qtbot)

    # when
    qtbot.mouseClick(window.btn_new_sql_request, QtCore.Qt.LeftButton)

    # then
    assert type(window.stackedWidget.currentWidget()) == SqlStepView, \
        "Should switch to SqlStepWidget"
