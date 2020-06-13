from app.sections.main import MainWindow


def test_show_all_folders(qtbot):
    # given
    window = MainWindow()

    # when
    window.show()
    qtbot.addWidget(window)

    # then
    assert window.cmb_folders.count() == 1
