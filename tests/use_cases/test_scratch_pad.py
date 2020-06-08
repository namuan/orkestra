# Test that the Fake FoldersView is called to update folder on App started event
from app.views.main_window import MainWindow


def test_save_scratchpad(qtbot):
    # given
    window = MainWindow()
    window.show()
    qtbot.addWidget(window)

    # when
    window.txt_scratch_pad.setText("Hello World")
    window.close()

    # then
    window.show()

    # then
    assert window.txt_scratch_pad.toPlainText() == "Hello World"
