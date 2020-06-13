from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialogButtonBox

from app.sections.main import MainWindow


def test_discard_envs_changes(qtbot):
    # given
    window = MainWindow()
    window.show()
    qtbot.addWidget(window)
    window.environment_view.show_dialog()
    no_of_environments = 5
    window.world.environment_store.clear_environments()

    # when
    for i in range(no_of_environments):
        qtbot.mouseClick(window.environment_view.btn_add_environment, QtCore.Qt.LeftButton)

    # then
    cancel_button = window.environment_view.btn_dialog_close.button(QDialogButtonBox.Cancel)
    qtbot.mouseClick(cancel_button, QtCore.Qt.LeftButton)

    # then
    environments = window.world.environment_store.get_environments()
    assert len(environments) == 0
