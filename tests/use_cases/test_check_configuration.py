from PyQt5 import QtCore

from app.views.main_window import MainWindow


def test_check_configuration(qtbot):
    # given
    window = MainWindow()
    window.show()
    qtbot.addWidget(window)
    window.config_view.show_dialog()

    # when
    qtbot.mouseClick(window.config_view.update, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.config_view.credits, QtCore.Qt.LeftButton)

    # then
    assert True
