import logging

import attr

from app.commands.add_step_command import AddStepCommand
from app.core.step_types import StepType
from app.core.uuid_utils import gen_uuid
from app.data import BaseEntity, BaseStore

STEP_RECORD_TYPE = "steps"


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
        step_db = table.find_one(name=STEP_RECORD_TYPE, step_id=step_id)
        # if not step_db:
        #     return None

        return StepEntity.from_json_str(step_db["object"])

    def get_steps(self):
        logging.info("Get All Steps")
        table = self.ds.table_for(STEP_RECORD_TYPE)
        steps_db = table.find(name=STEP_RECORD_TYPE)
        return {
            step_db["step_id"]: StepEntity.from_json_str(step_db["object"])
            for step_db in steps_db
        }

    def delete_all_steps(self):
        logging.info("Delete All Steps")
        table = self.ds.table_for(STEP_RECORD_TYPE)
        table.delete(name=STEP_RECORD_TYPE)
        self.ds.events.steps_deleted.emit()

    def delete_single_step(self, step_id):
        logging.info("Delete Step: {}".format(step_id))
        table = self.ds.table_for(STEP_RECORD_TYPE)
        table.delete(step_id=step_id)
        self.ds.events.step_deleted.emit(step_id)
