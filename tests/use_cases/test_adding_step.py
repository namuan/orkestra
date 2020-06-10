from app.views.main_window import MainWindow


def test_add_new_step(qtbot):
    # given
    window = MainWindow()
    window.show()
    qtbot.addWidget(window)

    # when
    window.steps_controller.trigger_add_step_command("HTTP")

    # then
    assert False
