import attr


@attr.s(auto_attribs=True)
class RunStepCommand:
    step_id: str
