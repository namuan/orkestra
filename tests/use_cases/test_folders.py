# Test that the Fake FoldersView is called to update folder on App started event
from app.views.main_window import MainWindow


def test_show_all_folders(qtbot):
    # given
    window = MainWindow()

    # when
    window.show()
    qtbot.addWidget(window)

    # then
    assert window.cmb_folders.count() == 1
