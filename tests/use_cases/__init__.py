from app.sections.main import MainWindow


def get_main_window():
    window = MainWindow()
    window.show()
    return window


def close_application(window):
    window.toolbar_controller.trigger_quit_application()


def wait(qtbot, time_ms=2000):
    qtbot.wait(time_ms)


def interact(qtbot):
    qtbot.stopForInteraction()
