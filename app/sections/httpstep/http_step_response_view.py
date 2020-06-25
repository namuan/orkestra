from app.sections.httpstep.http_step_response_controller import (
    HttpStepResponseController,
)


class HttpStepResponseView:
    def __init__(self, main_window, parent):
        self.controller = HttpStepResponseController(parent, main_window.world)
