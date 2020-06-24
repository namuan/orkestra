from app.sections.httpstep.http_step_request_controller import HttpStepRequestController


class HttpStepRequestView:
    def __init__(self, main_window, parent):
        self.controller = HttpStepRequestController(parent, main_window.world)
