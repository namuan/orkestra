from . import get_main_window


def test_show_all_folders(qtbot):
    # given
    window = get_main_window()

    # when
    window.show()
    qtbot.addWidget(window)

    # then
    assert window.cmb_folders.count() == 1, \
        "Unable to load Default folder"
