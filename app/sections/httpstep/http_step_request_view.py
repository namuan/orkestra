from app.commands.run_step_command import RunStepCommand
from app.sections.httpstep.http_step_request_controller import HttpStepRequestController
from app.sections.step.step_store import HttpStepEntity


class HttpStepRequestView:
    def __init__(self, main_window, parent):
        self.main_window = main_window
        self.parent = parent
        self.controller = HttpStepRequestController(self, main_window.world)

        # ui events
        self.parent.btn_send_request.pressed.connect(self.on_send_http_request)

    def object_to_form(self, step_entity):
        http_step_entity: HttpStepEntity = step_entity.step_data
        self.parent.cmb_http_method.setCurrentText(http_step_entity.http_method)
        self.parent.txt_http_url.setText(http_step_entity.http_url)

    def form_to_object(self):
        http_step_entity = HttpStepEntity(
            http_method=self.parent.cmb_http_method.currentText(),
            http_url=self.parent.txt_http_url.text(),
            http_headers=self.parent.lst_http_headers.items(),
            http_query_params=self.parent.lst_http_query_params.items(),
            http_form_params=self.parent.lst_http_form_params.items(),
            http_request_body=self.parent.txt_http_request_body.toPlainText(),
        )

        return http_step_entity

    def on_send_http_request(self):
        run_step_command = RunStepCommand(step_id=self.controller.current_step_id)
        self.controller.trigger_run_http_step(run_step_command)
