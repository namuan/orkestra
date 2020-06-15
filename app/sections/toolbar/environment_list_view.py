from .environment_list_controller import EnvironmentListController


class EnvironmentListView:
    def __init__(self, main_window):
        self.main_window = main_window
        self.world = main_window.world
        self.toolbar = main_window.toolbar_controller.toolbar
        self.controller = EnvironmentListController(self, self.main_window.world)

    def on_toolbar_selected_environment_changed(self, new_environment):
        if not new_environment:
            return

        self.controller.current_environment_changed(new_environment)

    def populate_environments(self, environments):
        environment_list_combo = self.get_environment_list_combo()
        environment_list_combo.clear()
        for environment in environments:
            environment_list_combo.addItem(environment.name)

    def set_toolbar_current_environment(self, new_environment):
        environment_list_combo = self.get_environment_list_combo()
        environment_list_combo.setCurrentText(new_environment)

    def get_environment_list_combo(self):
        toolbar_actions = self.toolbar.actions()
        list_action = next(
            act for act in toolbar_actions if act.text() == "Environmnents"
        )
        return list_action.defaultWidget()
