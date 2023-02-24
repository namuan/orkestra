import logging

from PyQt6.QtWidgets import QProxyStyle, QApplication
from PyQt6.QtCore import QFile, QFileInfo, QTextStream


def styles_from_file(filename):
    if QFileInfo(filename).exists():
        qss_file = QFile(filename)
        qss_file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text)
        content = QTextStream(qss_file).readAll()
        return content
    else:
        return None


class ThemeLoader(QProxyStyle):
    def __init__(self):
        super().__init__()

    def load_stylesheet(self, theme_mode):
        filename = ":/themes/{}.qss".format(theme_mode)

        styles = styles_from_file(filename)
        QApplication.instance().setStyleSheet(styles) if styles else self.log_error(
            filename
        )

    def log_error(self, styles_file):
        logging.error(f"Unable to read file from {styles_file}")
