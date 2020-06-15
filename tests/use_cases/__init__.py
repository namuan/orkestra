from app.sections.main import MainWindow


def get_main_window():
    window = MainWindow()
    window.show()
    return window


def close_application(window):
    window.toolbar_controller.trigger_quit_application()
