from app.views.main_window import MainWindow


def test_add_new_steps(qtbot):
    # given
    window = MainWindow()
    window.show()
    qtbot.addWidget(window)

    # when
    window.toolbar_controller.trigger_add_step_command("HTTP")
    window.toolbar_controller.trigger_add_step_command("SQL")

    # then
    assert window.lst_steps.model().rowCount() == 2
