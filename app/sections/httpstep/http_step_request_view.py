from app.sections.httpstep.http_step_request_controller import HttpStepRequestController
from app.sections.step.step_store import HttpStepEntity


class HttpStepRequestView:
    def __init__(self, main_window, parent):
        self.main_window = main_window
        self.parent = parent
        self.controller = HttpStepRequestController(self, main_window.world)

    def object_to_form(self, step_entity):
        http_step_entity: HttpStepEntity = step_entity.step_data
        self.parent.cmb_http_method.setCurrentText(http_step_entity.http_method)
        self.parent.txt_http_url.setText(http_step_entity.http_url)
