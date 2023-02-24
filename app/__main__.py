import sys
from PyQt6.QtWidgets import QApplication

from app import __version__, __appname__, __desktopid__
from app.sections.main import MainWindow
from app.themes.theme_provider import configure_theme


def main():
    app = QApplication(sys.argv)
    app.setApplicationVersion(__version__)
    app.setApplicationName(__appname__)
    app.setDesktopFileName(__desktopid__)

    window = MainWindow()
    configure_theme(app)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
