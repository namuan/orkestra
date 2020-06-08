import json
import logging

import attr
import cattr

from app.core.str_utils import plain_to_b64_str, b64_to_plain_str
from app.signals import AppEvents

APP_STATE_RECORD_TYPE = "app_state"


@attr.s(auto_attribs=True)
class AppState:
    record_type: str = APP_STATE_RECORD_TYPE
    selected_tool: str = ""
    scratch_note: str = ""

    @classmethod
    def from_json_str(cls, json_str):
        json_obj = json.loads(json_str)
        return cls.from_json(json_obj)

    @classmethod
    def from_json(cls, json_obj):
        if not json_obj:
            return cls()
        return cattr.structure(json_obj, cls)

    def to_json(self):
        return cattr.unstructure(self)

    def to_json_str(self):
        return json.dumps(self.to_json())


class AppStateStore:
    events: AppEvents()

    def __init__(self, data_store):
        self.ds = data_store
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
            return AppState()

        return AppState.from_json_str(app_state_db["object"])

    def update_selected_tool(self, selected_tool):
        logging.debug("Updating selected tool to {}".format(selected_tool))
        if not selected_tool:
            return

        self.app_state.selected_tool = selected_tool
        self.update_app_state_in_db()
        self.events.tool_switched.emit(selected_tool)

    def get_selected_tool(self):
        return self.app_state.selected_tool

    def update_scratch_note(self, scratch_note):
        logging.debug("Updating Scratch Pad: Characters: {}".format(len(scratch_note)))
        if not scratch_note:
            return

        self.app_state.scratch_note = plain_to_b64_str(scratch_note)
        self.update_app_state_in_db()

    def get_scratch_note(self):
        return b64_to_plain_str(self.app_state.scratch_note)
