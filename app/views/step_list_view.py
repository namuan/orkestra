from app.controllers import StepListController


class StepListView:
    def __init__(self, main_window):
        self.main_window = main_window
        self.controller = StepListController(self, self.main_window.world)
