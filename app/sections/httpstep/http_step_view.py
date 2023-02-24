from PyQt6.QtWidgets import QDialog

from app.generated.HttpStepWidget_ui import Ui_HttpStepWidget
from app.sections.httpstep.http_step_request_view import HttpStepRequestView
from app.sections.httpstep.http_step_response_view import HttpStepResponseView


class HttpStepView(QDialog, Ui_HttpStepWidget):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.setupUi(self)

        self.http_step_request_view = HttpStepRequestView(main_window, self)
        self.http_step_response_view = HttpStepResponseView(main_window, self)
