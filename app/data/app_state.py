import logging
from typing import Optional

import attr

from app.data import BaseEntity, BaseStore
from app.data.data_store import DataStore
from app.utils.str_utils import plain_to_b64_str, b64_to_plain_str

APP_STATE_RECORD_TYPE = "app_state"


@attr.s(auto_attribs=True)
class AppStateEntity(BaseEntity):
    record_type: str = APP_STATE_RECORD_TYPE
    selected_tool: str = ""
    scratch_note: str = ""
    selected_step_id: Optional[str] = None
    selected_environment: Optional[str] = None


class AppStateStore(BaseStore):
    def __init__(self, data_store: DataStore):
        super().__init__(data_store)
        self._app_state = self.get_app_state()

    @property
    def app_state(self):
        return self._app_state

    def update_app_state_in_db(self):
        table = self.ds.table_for(self.app_state.record_type)
        table.upsert(
            dict(name=self.app_state.record_type, object=self.app_state.to_json_str()),
            ["name"],
        )

    def get_app_state(self):
        table = self.ds.table_for(APP_STATE_RECORD_TYPE)
        app_state_db = table.find_one(name=APP_STATE_RECORD_TYPE)
        if not app_state_db:
            return AppStateEntity()

        return AppStateEntity.from_json_str(app_state_db["object"])

    def update_selected_step(self, selected_step_id):
        logging.debug("Update selected step to {}".format(selected_step_id))

        self.app_state.selected_step_id = selected_step_id
        self.update_app_state_in_db()
        self.ds.events.step_selection_changed.emit(selected_step_id)

    def update_selected_environment(self, new_selected_environment):
        logging.debug(
            "Update selected environment to {}".format(new_selected_environment)
        )
        self.app_state.selected_environment = new_selected_environment
        self.update_app_state_in_db()
        self.ds.events.environment_selection_changed.emit(new_selected_environment)

    def update_scratch_note(self, scratch_note):
        logging.debug("Updating Scratch Pad: Characters: {}".format(len(scratch_note)))
        if not scratch_note:
            return

        self.app_state.scratch_note = plain_to_b64_str(scratch_note)
        self.update_app_state_in_db()

    def get_scratch_note(self):
        return b64_to_plain_str(self.app_state.scratch_note)
