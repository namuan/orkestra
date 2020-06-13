from PyQt5 import QtCore

from . import get_main_window


def test_check_configuration(qtbot):
    # given
    window = get_main_window()
    qtbot.addWidget(window)
    window.config_view.show_dialog()

    # when
    qtbot.mouseClick(window.config_view.update, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.config_view.credits, QtCore.Qt.LeftButton)

    # then
    assert True
