import attr

from app.commands.add_step_command import AddStepCommand
from app.core.step_types import StepType
from app.core.uuid_utils import gen_uuid
from app.data import BaseEntity, BaseStore

STEP_RECORD_TYPE = "steps"


@attr.s(auto_attribs=True)
class StepEntity(BaseEntity):
    name: str
    id: str
    step_type: StepType
    record_type: str = STEP_RECORD_TYPE


class StepStore(BaseStore):
    def __init__(self, data_store):
        super().__init__(data_store)

    def add_step(self, add_step_command: AddStepCommand):
        step_entity = StepEntity(
            name=add_step_command.name,
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
        self.ds.events.step_added.emit(step_entity.id)
