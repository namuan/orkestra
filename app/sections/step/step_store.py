import logging

import attr

from app.commands.add_step_command import AddStepCommand
from app.core.step_types import StepType
from app.core.uuid_utils import gen_uuid
from app.data import BaseEntity, BaseStore

STEP_RECORD_TYPE = "steps"
DEFAULT_TITLE = "Change this"


def default_title(step_type: StepType):
    if step_type == StepType.HTTP:
        return "Get Request"
    elif step_type == StepType.SQL:
        return "Select All"


def default_description():
    return "Change description"


@attr.s(auto_attribs=True)
class StepEntity(BaseEntity):
    title: str
    description: str
    id: str
    step_type: StepType
    record_type: str = STEP_RECORD_TYPE


class StepStore(BaseStore):
    def __init__(self, data_store):
        super().__init__(data_store)

    def add_step(self, add_step_command: AddStepCommand):
        step_entity = StepEntity(
            title=default_title(add_step_command.step_type),
            description=default_description(),
            id=gen_uuid(),
            step_type=add_step_command.step_type,
        )
        table = self.ds.table_for(step_entity.record_type)
        table.upsert(
            dict(
                name=STEP_RECORD_TYPE,
                step_id=step_entity.id,
                object=step_entity.to_json_str(),
            ),
            ["step_id"],
        )
        logging.info("Upsert Step: {}".format(step_entity.id))
        self.ds.events.step_added.emit(step_entity.id)

    def get_step(self, step_id):
        logging.info("Get Step: {}".format(step_id))
        table = self.ds.table_for(STEP_RECORD_TYPE)
        obj_db = table.find_one(name=STEP_RECORD_TYPE, step_id=step_id)
        return StepEntity.from_json_str(obj_db["object"])