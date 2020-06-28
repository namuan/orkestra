from typing import Union, Optional

import attr

from app.sections.step.step_data_entities import HttpStepEntity, SqlStepEntity


@attr.s(auto_attribs=True)
class RunStepCommand:
    step_id: str
    step_entity: Optional[Union[HttpStepEntity, SqlStepEntity]] = None
