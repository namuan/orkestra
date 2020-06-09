class StepsController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.world = self.main_window.world

    def add_step(self, step_name):
        print("Adding step {}".format(step_name))
