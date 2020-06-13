from PyQt5 import QtCore

from app.views.main_window import MainWindow


def test_add_new_steps(qtbot):
    # given
    window = MainWindow()
    window.show()
    qtbot.addWidget(window)
    window.environment_view.show_dialog()
    no_of_environments = 5

    # when
    for i in range(no_of_environments):
        qtbot.mouseClick(window.environment_view.btn_add_environment, QtCore.Qt.LeftButton)

    # then
    assert window.environment_view.lst_environments.count() == no_of_environments

    # remove
    for i in range(no_of_environments):
        qtbot.mouseClick(window.environment_view.btn_remove_environment, QtCore.Qt.LeftButton)

    # then
    assert window.environment_view.lst_environments.count() == 0
