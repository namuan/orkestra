import attr

from app.core.step_types import StepType


@attr.s(auto_attribs=True)
class AddStepCommand:
    step_type: StepType
