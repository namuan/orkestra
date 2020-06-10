import attr

from app.core.step_types import StepType


@attr.s(auto_attribs=True)
class AddStepCommand:
    name: str
    step_type: StepType
