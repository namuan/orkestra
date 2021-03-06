from . import get_main_window


def test_save_scratchpad(qtbot):
    # given
    window = get_main_window()
    qtbot.addWidget(window)

    # when
    window.txt_scratch_pad.setText("Hello World")
    window.close()

    # then
    window.show()

    # then
    assert window.txt_scratch_pad.toPlainText() == "Hello World", \
        "ScratchPad not being saved in database"
